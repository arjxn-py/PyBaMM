FROM python:3.9

RUN useradd -m -s /bin/bash pybamm
USER pybamm

WORKDIR /home/pybamm/

COPY pybamm-24.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl /home/pybamm/tmp/

RUN pip install /home/pybamm/tmp/pybamm-24.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

ENV SUNDIALS_INST=/home/pybamm/.local
ENV LD_LIBRARY_PATH=/home/pybamm/.local/lib

COPY test.py /app/

WORKDIR /app

CMD ["python", "test.py"]
