#!/bin/bash

pushd jasper
make clean
make distclean
rm -rf install
popd
