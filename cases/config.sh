#!/bin/bash

#
# You should want to set LLVM_HOME and adjust
# the path for afl tools in LCC/LCXX variables
# Also, depending on your goals, adjust IA32_TARGET
# and/or ASAN_BUILD.
#
#

# TODO: Should include gcc as well.

LLVM_HOME=/usr

AFL_HOME=/home/arr/AFLplusplus-git

#
# Set to non-zero for AFL compilation mode
#
AFL_ON=1

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
 echo "AFL compilation: disabled"

 LCC=${LLVM_HOME}/bin/clang
 LCXX=${LLVM_HOME}/bin/clang++
else
 echo "AFL compilation: enabled"

 LCC=${AFL_HOME}/afl-clang-fast
 LCXX=${AFL_HOME}/afl-clang-fast++
# LCC=${AFL_HOME}/afl-clang
# LCXX=${AFL_HOME}/afl-clang
fi

#
# If you do not want ASan, make this empty
#
ASAN_BUILD="-fsanitize=address"

#
# If you want to compile for x86-64, just leave empty
#
IA32_TARGET="-m32 -march=i686"

#
# Set these, hopefully, for CFLAGS and CXXFLAGS
#
# Note: 32-bit for ASan + AFL
#
LCFLAGS="${IA32_TARGET} -nopie -fno-stack-protector ${ASAN_BUILD}"
LCXXFLAGS="${IA32_TARGET} -nopie -fno-stack-protector ${ASAN_BUILD}"

#LCFLAGS="-nopie -fno-stack-protector"
#LCXXFLAGS="-nopie -fno-stack-protector"

#
# Set for any ./configure script options --prefix is done
# more in the build.sh of the application itself instead of
# at this level.
#
CONFIGFLAGS=""
