#!/bin/bash -e

echo ""
echo "./check-tf.sh - Checks Tensorflow installation with GPU"

source enter.sh
python src/check-tf.py

echo "FINISHED check-tf.sh! EVERYTHING SEEMS TO BE OK"
echo ""
