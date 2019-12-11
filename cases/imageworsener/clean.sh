#!/bin/bash

pushd imageworsener-1.3.0
make clean 
make distclean 
rm -rf install 
rm -rf autom4te.cache
popd
