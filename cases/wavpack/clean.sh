#!/bin/bash

pushd wavpack
make clean
make distclean
rm -rf install
rm -rf autom4te.cache
popd
rm /tmp/delete*.wav

