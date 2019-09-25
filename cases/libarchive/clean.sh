#!/bin/bash

pushd libarchive
make clean
make distclean
rm -rf install
popd
