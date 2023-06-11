#
# Test the base experiment class
#
from tests import TestCase
import pybamm
import unittest


class TestExperiment(TestCase):
    def test_cycle_unpacking(self):
        experiment = pybamm.Experiment(
            [
                ("Discharge at C/20 for 0.5 hours", "Charge at C/5 for 45 minutes"),
                ("Discharge at C/20 for 0.5 hours"),
                "Charge at C/5 for 45 minutes",
            ]
        )
        self.assertEqual(
            [step.to_dict() for step in experiment.operating_conditions_steps],
            [
                {
                    "value": 0.05,
                    "type": "C-rate",
                    "duration": 1800.0,
                    "period": 60.0,
                    "temperature": None,
                    "description": "Discharge at C/20 for 0.5 hours",
                    "termination": [],
                    "tags": [],
                },
                {
                    "value": -0.2,
                    "type": "C-rate",
                    "duration": 2700.0,
                    "period": 60.0,
                    "temperature": None,
                    "description": "Charge at C/5 for 45 minutes",
                    "termination": [],
                    "tags": [],
                },
                {
                    "value": 0.05,
                    "type": "C-rate",
                    "duration": 1800.0,
                    "period": 60.0,
                    "temperature": None,
                    "description": "Discharge at C/20 for 0.5 hours",
                    "termination": [],
                    "tags": [],
                },
                {
                    "value": -0.2,
                    "type": "C-rate",
                    "duration": 2700.0,
                    "period": 60.0,
                    "temperature": None,
                    "description": "Charge at C/5 for 45 minutes",
                    "termination": [],
                    "tags": [],
                },
            ],
        )
        self.assertEqual(experiment.cycle_lengths, [2, 1, 1])

    def test_str_repr(self):
        conds = ["Discharge at 1 C for 20 seconds", "Charge at 0.5 W for 10 minutes"]
        experiment = pybamm.Experiment(conds)
        self.assertEqual(
            str(experiment),
            "[('Discharge at 1 C for 20 seconds',)"
            + ", ('Charge at 0.5 W for 10 minutes',)]",
        )
        self.assertEqual(
            repr(experiment),
            "pybamm.Experiment([('Discharge at 1 C for 20 seconds',)"
            + ", ('Charge at 0.5 W for 10 minutes',)])",
        )

    def test_bad_strings(self):
        with self.assertRaisesRegex(
            TypeError, "Operating conditions should be strings or _Step objects"
        ):
            pybamm.Experiment([1, 2, 3])
        with self.assertRaisesRegex(
            TypeError, "Operating conditions should be strings or _Step objects"
        ):
            pybamm.Experiment([(1, 2, 3)])

    def test_deprecations(self):
        with self.assertRaisesRegex(ValueError, "cccv_handling"):
            pybamm.Experiment([], cccv_handling="something")
        with self.assertRaisesRegex(ValueError, "drive_cycles"):
            pybamm.Experiment([], drive_cycles="something")

    def test_termination(self):
        experiment = pybamm.Experiment(["Discharge at 1 C for 20 seconds"])
        self.assertEqual(experiment.termination, {})

        experiment = pybamm.Experiment(
            ["Discharge at 1 C for 20 seconds"], termination="80.7% capacity"
        )
        self.assertEqual(experiment.termination, {"capacity": (80.7, "%")})

        experiment = pybamm.Experiment(
            ["Discharge at 1 C for 20 seconds"], termination="80.7 % capacity"
        )
        self.assertEqual(experiment.termination, {"capacity": (80.7, "%")})

        experiment = pybamm.Experiment(
            ["Discharge at 1 C for 20 seconds"], termination="4.1Ah capacity"
        )
        self.assertEqual(experiment.termination, {"capacity": (4.1, "Ah")})

        experiment = pybamm.Experiment(
            ["Discharge at 1 C for 20 seconds"], termination="4.1 A.h capacity"
        )
        self.assertEqual(experiment.termination, {"capacity": (4.1, "Ah")})

        experiment = pybamm.Experiment(
            ["Discharge at 1 C for 20 seconds"], termination="3V"
        )
        self.assertEqual(experiment.termination, {"voltage": (3, "V")})

        experiment = pybamm.Experiment(
            ["Discharge at 1 C for 20 seconds"], termination=["3V", "4.1Ah capacity"]
        )
        self.assertEqual(
            experiment.termination, {"voltage": (3, "V"), "capacity": (4.1, "Ah")}
        )

        with self.assertRaisesRegex(ValueError, "Only capacity"):
            experiment = pybamm.Experiment(
                ["Discharge at 1 C for 20 seconds"], termination="bla bla capacity bla"
            )
        with self.assertRaisesRegex(ValueError, "Only capacity"):
            experiment = pybamm.Experiment(
                ["Discharge at 1 C for 20 seconds"], termination="4 A.h something else"
            )
        with self.assertRaisesRegex(ValueError, "Capacity termination"):
            experiment = pybamm.Experiment(
                ["Discharge at 1 C for 20 seconds"], termination="1 capacity"
            )

    def test_search_tag(self):
        s = pybamm.step.string
        experiment = pybamm.Experiment(
            [
                (s("Discharge at 1C for 0.5 hours", tags=["tag1"]),),
                s("Discharge at C/20 for 0.5 hours", tags=["tag2", "tag3"]),
                (
                    s("Charge at 0.5 C for 45 minutes", tags=["tag2"]),
                    s("Discharge at 1 A for 0.5 hours", tags=["tag3"]),
                ),
                s("Charge at 200 mA for 45 minutes", tags=["tag5"]),
                (
                    s("Discharge at 1W for 0.5 hours", tags=["tag4"]),
                    s("Charge at 200mW for 45 minutes", tags=["tag4"]),
                ),
                s("Rest for 10 minutes", tags=["tag1", "tag3", "tag4"]),
            ]
        )

        self.assertEqual(experiment.search_tag("tag1"), [0, 5])
        self.assertEqual(experiment.search_tag("tag2"), [1, 2])
        self.assertEqual(experiment.search_tag("tag3"), [1, 2, 5])
        self.assertEqual(experiment.search_tag("tag4"), [4, 5])
        self.assertEqual(experiment.search_tag("tag5"), [3])
        self.assertEqual(experiment.search_tag("no_tag"), [])


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
