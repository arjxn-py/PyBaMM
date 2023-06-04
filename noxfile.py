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
    session.run("pip", "install", "-e", ".[dev]")
    if sys.platform != "win32" or sys.platform != "darwin":
        session.run("pybamm_install_jax")
    session.run("coverage", "run", "run-tests.py", "--nosub")
    session.run("coverage", "combine")
    session.run("coverage", "xml")


@nox.session(name="integration", reuse_venv=True)
def run_integration(session):
    session.run("pip", "install", "-e", ".[dev]")
    session.run("python", "run-tests.py", "--integration")


@nox.session(name="doctests", reuse_venv=True)
def run_doctests(session):
    session.run("pip", "install", "-e", ".[docs]")
    session.run("python", "run-tests.py", "--doctest")


@nox.session(name="doctests", reuse_venv=True)
def run_doctests(session):
    session.run("pip", "install", "-e", ".[docs]")
    session.run("python", "run-tests.py", "--doctest")


@nox.session(name="unit", reuse_venv=True)
def run_doctests(session):
    session.run("pip", "install", "-e", ".[dev]")
    session.run("pybamm_install_jax")
    session.run("python", "run-tests.py", "--unit")


@nox.session(name="mac-windows-unit", reuse_venv=True)
def run_mac_windows_unit(session):
    session.run("pip", "install", "-e", ".[dev]")
    session.run("python", "run-tests.py", "--unit")


@nox.session(name="mac-windows-integration", reuse_venv=True)
def run_mac_windows_integration(session):
    session.run("pip", "install", "-e", ".[dev]")
    session.run("python", "run-tests.py", "--integration")


@nox.session(name="examples", reuse_venv=True)
def run_examples(session):
    session.run("pip", "install", "-e", ".[dev]")
    session.run("python", "run-tests.py", "--examples")
