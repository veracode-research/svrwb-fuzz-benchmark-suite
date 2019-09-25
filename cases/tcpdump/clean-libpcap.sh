#!/bin/bash

pushd libpcap
make clean
make distclean
rm -rf install
popd

