#!/bin/bash -e

echo ""
echo "./check-torch.sh - Checks PyTorch installation with GPU"

source enter.sh
python src/check-torch.py

echo "FINISHED check-torch.sh! EVERYTHING SEEMS TO BE OK"
echo ""
