Install from source (developer install)
=========================================

.. contents::

This page describes the build and installation of PyBaMM from the source code, available on GitHub. Note that this is **not the recommended approach for most users** and should be reserved to people wanting to participate in the development of PyBaMM, or people who really need to use bleeding-edge feature(s) not yet available in the latest released version. If you do not fall in the two previous categories, you would be better off installing PyBaMM using pip or conda.

Lastly, familiarity with the Python ecosystem is recommended (pip, virtualenvs).
Here is a gentle introduction/refresher: `Python Virtual Environments: A Primer <https://realpython.com/python-virtual-environments-a-primer/>`_.


Prerequisites
---------------

The following instructions are valid for both GNU/Linux distributions and MacOS.
If you are running Windows, consider using the `Windows Subsystem for Linux (WSL) <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.

To obtain the PyBaMM source code, clone the GitHub repository

.. code:: bash

	  git clone https://github.com/pybamm-team/PyBaMM.git

or download the source archive on the repository's homepage.

To install PyBaMM, you will need:

- Python 3 (PyBaMM supports versions 3.8, 3.9, 3.10, and 3.11)
- The Python headers file for your current Python version.
- A BLAS library (for instance `openblas <https://www.openblas.net/>`_).
- A C compiler (ex: ``gcc``).
- A Fortran compiler (ex: ``gfortran``).

You can install the above with

.. tab:: Ubuntu

	.. code:: bash

		sudo apt install python3.X python3.X-dev libopenblas-dev gcc gfortran

	Where ``X`` is the version sub-number.

.. tab:: MacOS

	.. code:: bash

		brew install python openblas gcc gfortran libomp

Finally, we recommend using `Nox <https://nox.thea.codes/en/stable/>`_.
You can install it with

.. code:: bash

	  python3.X -m pip install --user "nox"

Depending on your operating system, you may or may not have ``pip`` installed along Python.
If ``pip`` is not found, you probably want to install the ``python3-pip`` package.

Installing the build-time requirements
--------------------------------------

PyBaMM comes with a DAE solver based on the IDA solver provided by the SUNDIALS library.
To use this solver, you must make sure that you have the necessary SUNDIALS components
installed on your system.

The IDA-based solver is currently unavailable on windows.
If you are running windows, you can simply skip this section and jump to :ref:`pybamm-install`.

.. code:: bash

	  # in the PyBaMM/ directory
	  nox -s pybamm-requires

This will download, compile and install the SuiteSparse and SUNDIALS libraries.
Both libraries are installed in ``~/.local``.

Manual install of build time requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you'd rather do things yourself,

1. Make sure you have CMake installed
2. Compile and install SuiteSparse (PyBaMM only requires the ``KLU`` component).
3. Compile and install SUNDIALS.
4. Clone the pybind11 repository in the ``PyBaMM/`` directory (make sure the directory is named ``pybind11``).
	 

PyBaMM ships with a Python script that automates points 2. and 3. You can run it with

.. code:: bash

	  python scripts/install_KLU_Sundials.py

.. _pybamm-install:

Installing PyBaMM
-----------------

You should now have everything ready to build and install PyBaMM successfully.

Using Nox (recommended)
~~~~~~~~~~~~~~~~~~~~~~~

.. tab:: GNU/Linux, MacOS & Windows

	.. code:: bash

		# in the PyBaMM/ directory
		nox -s dev

This creates a virtual environment ``.nox/dev`` inside the ``PyBaMM/`` directory.
It comes ready with PyBaMM and some useful development tools like `pre-commit <https://pre-commit.com/>`_ and `black <https://black.readthedocs.io/en/stable/>`_.

You can now activate the environment with

.. tab:: GNU/Linux and MacOS

	.. code:: bash

		source .nox/dev/bin/activate

.. tab:: Windows

	.. code:: bash

	  	.nox\dev\Scripts\activate.bat # (Windows)

and run the tests to check your installation.

Manual install
~~~~~~~~~~~~~~

From the ``PyBaMM/`` directory, you can install PyBaMM using ``python setup.py install`` or 

.. code:: bash

	  pip install .

If you intend to contribute to the development of PyBaMM, it is convenient to install in "editable mode", along with useful tools for development and documentation:

.. code:: bash

	  pip install -e .[dev,docs]

If you are using ``zsh``, you would need to use different pattern matching:

.. code:: bash

	  pip install -e .'[dev,docs]'

Running the tests
--------------------

Using Nox (recommended)
~~~~~~~~~~~~~~~~~~~~~~~

You can use Nox to run the unit tests and example notebooks in isolated virtual environments.

The default command

.. tab:: GNU/Linux, MacOS & Windows

	.. code:: bash

		nox -s tests

will run the full test suite (integration and unit tests).
This can take several minutes.

It is often sufficient to run the unit tests only. To do so, use

.. tab:: GNU/Linux, MacOS & Windows

   .. code:: bash

    	nox -s unit

Using the test runner 
~~~~~~~~~~~~~~~~~~~~~~

You can run unit tests for PyBaMM using

.. code:: bash

	  # in the PyBaMM/ directory
	  python run-tests.py --unit


The above starts a sub-process using the current python interpreter (i.e. using your current
Python environment) and run the unit tests. This can take a few minutes.

You can also use the test runner to run the doctests:

.. code:: bash

	  python run-tests.py --doctest

There is more to the PyBaMM test runner. To see a list of all options, type

.. code:: bash

	  python run-tests.py --help

How to build the PyBaMM documentation
-------------------------------------

The documentation is built using

.. code:: bash

	  nox -s docs

This will build the documentation and serve it locally (thanks to `sphinx-autobuild <https://github.com/GaretJax/sphinx-autobuild>`_) for preview.
The preview will be updated automatically following changes.

Doctests, examples, style and coverage
--------------------------------------

.. tab:: GNU/Linux, MacOS & Windows

	``Nox`` can also be used to run the following commands:

	- ``nox -s examples``: Run the example scripts in ``examples/scripts``.
	- ``nox -s doctests``: Run doctests.


Use ``nox -s coverage`` to measure current test coverage on all platforms.
