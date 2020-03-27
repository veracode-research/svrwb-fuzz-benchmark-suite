#!/bin/bash

pushd wavpack-5.0.0
make clean
make distclean
rm -rf install
rm -rf autom4te.cache
rm -rf src/.deps/
popd

#rm /tmp/delete*.wav

