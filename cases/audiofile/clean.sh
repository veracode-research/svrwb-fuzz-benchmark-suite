#!/bin/bash

#rm -f lame_crash_UNK010.mp3 lame_crash_UNK011.mp3 lame_crash_UNK012.mp3 *.mp3.mp3
pushd audiofile-0.3.6
make clean
make distclean
rm -rf install
rm -rf config.log

popd

