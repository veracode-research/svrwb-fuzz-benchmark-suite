#!/bin/bash

pushd ytnef
make clean
make distclean
rm -rf install autom4te.cache
popd

