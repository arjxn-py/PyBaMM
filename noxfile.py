import nox
import os
import sys

@nox.session(name="pybamm-requires")
def run_unit_tests(session):
    if sys.platform != "win32" or sys.platform != "darwin":
        session.install("wget","cmake")
        session.run("python", "scripts/install_KLU_Sundials.py")
        session.run("git", "clone" "https://github.com/pybind/pybind11.git", "/pybind11", external=True)
