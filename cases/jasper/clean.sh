#!/bin/bash

pushd jasper-1.701.0
make clean
make distclean
rm -rf install
rm data/Makefile.in
popd
