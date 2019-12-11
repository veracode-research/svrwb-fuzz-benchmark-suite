#!/bin/bash

#
# You should want to set LLVM_HOME and adjust
# the path for afl tools in LCC/LCXX variables
#

# TODO: Should include gcc as well.

LLVM_HOME=/usr

#
# Set to non-zero for AFL compilation mode
#
AFL_ON=0

#
# These will be the value passed to AFL_CC and AFL_CXX
# when building with CC as afl-${CC}
#
ACC=${LLVM_HOME}/bin/clang
ACXX=${LLVM_HOME}/bin/clang++

#
# Set LCC/LCXX for AFL vs no AFL as they will be CC and CXX
#
#
if [ "$AFL_ON" -eq "0" ]; then
 echo "AFL compilation disabled"
 LCC=${LLVM_HOME}/bin/clang
 LCXX=${LLVM_HOME}/bin/clang++
else
 echo "AFL compilation enabled"
 LCC=/home/arr/aflgit/AFL/afl-clang
 LCXX=/home/arr/aflgit/AFL/afl-clang
# LCC=/home/arr/aflgit/AFL/afl-clang-fast
# LCXX=/home/arr/aflgit/AFL/afl-clang-fast++
fi

#
# Set these, hopefully, for CFLAGS and CXXFLAGS
# Sigh... the -m32 is for ASAN memory save, but is that ok?
#
#
LCFLAGS="-nopie -fno-stack-protector -fsanitize=address"
LCXXFLAGS="-nopie -fno-stack-protector -fsanitize=address"
#LCFLAGS="-nopie -fno-stack-protector"
#LCXXFLAGS="-nopie -fno-stack-protector"

#
# Set for any ./configure script options --prefix is done
# more in the build.sh of the application itself instead of
# at this level.
#
CONFIGFLAGS=""
