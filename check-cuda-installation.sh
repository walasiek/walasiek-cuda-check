#!/bin/bash -e

echo ""
echo "./check-cuda-installation.sh - Checks general CUDA installation in OS"

echo "Checking nvcc..."
nvcc --version > /dev/null

echo "Checking nvidia-smi"
nvidia-smi > /dev/null

echo "FINISHED check-cuda-installation.sh! EVERYTHING SEEMS TO BE OK"
echo ""
