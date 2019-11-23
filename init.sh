#!/bin/sh

virtualenv --python=python3 venv
source venv/bin/activate

if [ $(pip freeze | grep Pillow | wc -l) -eq "0" ]; then
    pip install Pillow
fi
