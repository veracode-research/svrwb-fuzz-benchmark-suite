#!/bin/bash

pushd imageworsener
make clean 
make distclean 
rm -rf install 
rm -rf autom4te.cache
popd
