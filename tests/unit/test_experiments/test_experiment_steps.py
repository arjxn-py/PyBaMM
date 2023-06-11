#
# Test the experiment steps
#
import pybamm
import unittest
import numpy as np


class TestExperimentSteps(unittest.TestCase):
    def test_step(self):
        step = pybamm.step._Step("current", 1, duration=3600)
        self.assertEqual(step.type, "current")
        self.assertEqual(step.value, 1)
        self.assertEqual(step.duration, 3600)
        self.assertEqual(step.termination, [])
        self.assertEqual(step.period, None)
        self.assertEqual(step.temperature, None)
        self.assertEqual(step.tags, [])

        step = pybamm.step._Step(
            "voltage",
            1,
            duration="1h",
            termination="2.5V",
            period="1 minute",
            temperature=298.15,
            tags="test",
        )
        self.assertEqual(step.type, "voltage")
        self.assertEqual(step.value, 1)
        self.assertEqual(step.duration, 3600)
        self.assertEqual(step.termination, [{"type": "voltage", "value": 2.5}])
        self.assertEqual(step.period, 60)
        self.assertEqual(step.temperature, 298.15)
        self.assertEqual(step.tags, ["test"])

        step = pybamm.step._Step("current", 1, temperature="298K")
        self.assertEqual(step.temperature, 298)

        with self.assertRaisesRegex(ValueError, "temperature units"):
            step = pybamm.step._Step("current", 1, temperature="298T")

    def test_specific_steps(self):
        current = pybamm.step.current(1)
        self.assertIsInstance(current, pybamm.step._Step)
        self.assertEqual(current.type, "current")
        self.assertEqual(current.value, 1)
        self.assertEqual(str(current), repr(current))

        c_rate = pybamm.step.c_rate(1)
        self.assertIsInstance(c_rate, pybamm.step._Step)
        self.assertEqual(c_rate.type, "C-rate")
        self.assertEqual(c_rate.value, 1)

        voltage = pybamm.step.voltage(1)
        self.assertIsInstance(voltage, pybamm.step._Step)
        self.assertEqual(voltage.type, "voltage")
        self.assertEqual(voltage.value, 1)

        rest = pybamm.step.rest()
        self.assertIsInstance(rest, pybamm.step._Step)
        self.assertEqual(rest.type, "current")
        self.assertEqual(rest.value, 0)

        power = pybamm.step.power(1)
        self.assertIsInstance(power, pybamm.step._Step)
        self.assertEqual(power.type, "power")
        self.assertEqual(power.value, 1)

        resistance = pybamm.step.resistance(1)
        self.assertIsInstance(resistance, pybamm.step._Step)
        self.assertEqual(resistance.type, "resistance")
        self.assertEqual(resistance.value, 1)

    def test_step_string(self):
        steps = [
            "Discharge at 1C for 0.5 hours",
            "Discharge at C/20 for 1h (2 minute period)",
            "Charge at 0.5 C for 45 minutes",
            "Discharge at 1 A for 0.5 hours",
            "Charge at 200 mA for 45 minutes",
            "Discharge at 1W for 0.5 hours",
            "Charge at 200mW for 45 minutes",
            "Rest for 10 minutes",
            "Hold at 1V for 20 seconds",
            "Charge at 1 C until 4.1V",
            "Hold at 4.1 V until 50mA",
            "Hold at 3V until C/50",
            "Discharge at C/3 for 2 hours or until 2.5 V",
        ]

        expected_result = [
            {
                "type": "C-rate",
                "value": 1.0,
                "duration": 1800.0,
                "termination": [],
            },
            {
                "type": "C-rate",
                "value": 0.05,
                "duration": 3600.0,
                "termination": [],
                "period": 120,
            },
            {
                "type": "C-rate",
                "value": -0.5,
                "duration": 2700.0,
                "termination": [],
            },
            {
                "value": 1.0,
                "type": "current",
                "duration": 1800.0,
                "termination": [],
            },
            {
                "value": -0.2,
                "type": "current",
                "duration": 2700.0,
                "termination": [],
            },
            {
                "value": 1.0,
                "type": "power",
                "duration": 1800.0,
                "termination": [],
            },
            {
                "value": -0.2,
                "type": "power",
                "duration": 2700.0,
                "termination": [],
            },
            {
                "value": 0,
                "type": "current",
                "duration": 600.0,
                "termination": [],
            },
            {
                "value": 1,
                "type": "voltage",
                "duration": 20.0,
                "termination": [],
            },
            {
                "type": "C-rate",
                "value": -1,
                "duration": None,
                "termination": [{"type": "voltage", "value": 4.1}],
            },
            {
                "value": 4.1,
                "type": "voltage",
                "duration": None,
                "termination": [{"type": "current", "value": 0.05}],
            },
            {
                "value": 3,
                "type": "voltage",
                "duration": None,
                "termination": [{"type": "C-rate", "value": 0.02}],
            },
            {
                "type": "C-rate",
                "value": 1 / 3,
                "duration": 7200.0,
                "termination": [{"type": "voltage", "value": 2.5}],
            },
        ]

        for step, expected in zip(steps, expected_result):
            print(step)
            actual = pybamm.step.string(step).to_dict()
            for k in expected.keys():
                # useful form for debugging
                self.assertEqual([k, expected[k]], [k, actual[k]])

        with self.assertRaisesRegex(ValueError, "Period cannot be"):
            pybamm.step.string(
                "Discharge at 1C for 1 hour (1 minute period)", period=60
            )

        with self.assertRaisesRegex(ValueError, "Temperature must be"):
            pybamm.step.string("Discharge at 1C for 1 hour at 298.15oC")

    def test_drive_cycle(self):
        # Import drive cycle from file
        drive_cycle = np.array([np.arange(10), np.arange(10)]).T

        # Create steps
        drive_cycle_step = pybamm.step.current(drive_cycle, temperature="-5oC")
        # Check drive cycle operating conditions
        self.assertEqual(drive_cycle_step.type, "current")
        self.assertEqual(drive_cycle_step.duration, 9)
        self.assertEqual(drive_cycle_step.period, 1)
        self.assertEqual(drive_cycle_step.temperature, 273.15 - 5)

        bad_drive_cycle = np.ones((10, 3))
        with self.assertRaisesRegex(ValueError, "Drive cycle must be a 2-column array"):
            pybamm.step.current(bad_drive_cycle)

    def test_drive_cycle_duration(self):
        # Import drive cycle from file
        drive_cycle = np.array([np.arange(10), np.arange(10)]).T

        # Check duration longer than drive cycle data
        # Create steps
        drive_cycle_step = pybamm.step.current(
            drive_cycle, duration=20, temperature="-5oC"
        )
        # Check drive cycle operating conditions
        self.assertEqual(drive_cycle_step.type, "current")
        self.assertEqual(drive_cycle_step.duration, 20)
        self.assertEqual(drive_cycle_step.period, 1)
        self.assertEqual(drive_cycle_step.temperature, 273.15 - 5)

        # Check duration shorter than drive cycle data
        # Create steps
        drive_cycle_step = pybamm.step.current(
            drive_cycle, duration=5, temperature="-5oC"
        )
        # Check drive cycle operating conditions
        self.assertEqual(drive_cycle_step.type, "current")
        self.assertEqual(drive_cycle_step.duration, 5)
        self.assertEqual(drive_cycle_step.period, 1)
        self.assertEqual(drive_cycle_step.temperature, 273.15 - 5)

    def test_bad_strings(self):
        with self.assertRaisesRegex(TypeError, "Input to step.string"):
            pybamm.step.string(1)
        with self.assertRaisesRegex(TypeError, "Input to step.string"):
            pybamm.step.string((1, 2, 3))
        with self.assertRaisesRegex(ValueError, "Operating conditions must"):
            pybamm.step.string("Discharge at 1 A at 2 hours")
        with self.assertRaisesRegex(ValueError, "drive cycles"):
            pybamm.step.string("Run at 1 A for 2 hours")
        with self.assertRaisesRegex(ValueError, "Instruction must be"):
            pybamm.step.string("Play at 1 A for 2 hours")
        with self.assertRaisesRegex(ValueError, "Operating conditions must"):
            pybamm.step.string("Do at 1 A")
        with self.assertRaisesRegex(ValueError, "Instruction"):
            pybamm.step.string("Cell Charge at 1 A for 2 hours")
        with self.assertRaisesRegex(ValueError, "units must be"):
            pybamm.step.string("Discharge at 1 B for 2 hours")
        with self.assertRaisesRegex(ValueError, "time units must be"):
            pybamm.step.string("Discharge at 1 A for 2 years")


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
