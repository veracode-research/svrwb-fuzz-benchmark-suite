#!/bin/bash

pushd libarchive+81ce2c24f9fec640740de9bcea920ab71ef89059
make clean
make distclean
rm -rf install
rm -rf Makefile.in bsdcat build   \
	cat/test/list.h  \
        config.h.in  \
        config.log  \
        configure   \
        autom4te.cache/
popd
