#!/bin/bash

pushd ytnef-1.9.2
make clean
make distclean
rm -rf install autom4te.cache
popd

