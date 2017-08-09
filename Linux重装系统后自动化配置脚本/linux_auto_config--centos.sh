#!/usr/bin/env bash

# build development environment

# all
yum groupinstall "Development Tools"  

# mini
yum install -y gcc g++ kernel-devel  