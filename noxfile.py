import nox
import os
import sys


@nox.session(name="pybamm-requires")
def run_pybamm_requires(session):
    if sys.platform != "win32" or sys.platform != "darwin":
        session.install("wget", "cmake")
        session.run("python", "scripts/install_KLU_Sundials.py")
        session.run(
            "git",
            "clone",
            "https://github.com/pybind/pybind11.git",
            "pybind11/",
            external=True,
        )


@nox.session(name="coverage")
def run_coverage(session):
    homedir = os.getenv("HOME")
    session.env["SUNDIALS_INST"] = session.env.get("SUNDIALS_INST", f"{homedir}/.local")
    session.env[
        "LD_LIBRARY_PATH"
    ] = f"{homedir}/.local/lib:{session.env.get('LD_LIBRARY_PATH')}"
    session.install("coverage", "scikits.odes")
    if sys.platform != "win32" or sys.platform != "darwin":
        session.run("pybamm_install_jax")
    session.run("coverage", "run", "run-tests.py", "--nosub")
    session.run("coverage", "combine")
    session.run("coverage", "xml")
