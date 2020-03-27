#!/bin/bash

SRC=audiofile-0.3.6

#rm -f lame_crash_UNK010.mp3 lame_crash_UNK011.mp3 lame_crash_UNK012.mp3 *.mp3.mp3
pushd ${SRC}
make clean
make distclean
rm -rf install
rm -rf autom4te.cache/
popd

