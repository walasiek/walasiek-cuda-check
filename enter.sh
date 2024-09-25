#!/bin/bash

# Run to create virtualenv for this repo
# If virtualenv is already created then activate it
# Params:
#   none

ENV_DIRNAME=walasiek-cuda-check
VIRTUALENV_DIR=$HOME/virtualenv/$ENV_DIRNAME

if [[ ! -d $VIRTUALENV_DIR ]]; then
    virtualenv -p python3 $VIRTUALENV_DIR
    source $VIRTUALENV_DIR/bin/activate
    pip install -r requirements.txt
else
    export PYTHONPATH=$PYTHONPATH:`pwd`
    source $VIRTUALENV_DIR/bin/activate
fi
