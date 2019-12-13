#!/bin/bash

#rm -f lame_crash_UNK010.mp3 lame_crash_UNK011.mp3 lame_crash_UNK012.mp3 *.mp3.mp3

pushd lame-3.99.5
rm -rf install
make clean
make distclean
patch -p0 -R < configure-patch.diff
rm configure-patch.diff configure.orig
popd

