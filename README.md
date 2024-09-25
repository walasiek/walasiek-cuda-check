Overview
========

Utils to check CUDA installation on my machines.

Checkers to be checked
======================

You can run:

   ./check-all.sh

Or run each step separately:

   1. check-cuda-installation.sh - checks if drivers are properly installed
   2. check-tf.sh - checks if Tensorflow config is ok
   3. check-torch.sh - checks PyTorch config is ok

Ubuntu 24.04 tips
=================

The following packages might be needed:

    sudo apt install nvidia-cuda-toolkit
    sudo apt install nvidia-cudnn
