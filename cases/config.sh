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
GCC_HOME=/usr

AFL_HOME=/home/arr/AFLplusplus-git

#
# Set to non-zero for AFL compilation mode
#
AFL_ON=0

#
# Turn to non-zero to enable GCC
#
USE_GCC=0


#
# These will be the value passed to AFL_CC and AFL_CXX
# when building with CC as afl-${CC}
#
if [ "$USE_GCC" -eq "0" ]; then
 echo "Using CLANG"
 ACC=${LLVM_HOME}/bin/clang
 ACXX=${LLVM_HOME}/bin/clang++
else
 echo "Using GCC"
 ACC=${GCC_HOME}/bin/gcc
 ACXX=${GCC_HOME}/bin/g++
fi

#
# Set LCC/LCXX for AFL vs no AFL as they will be CC and CXX
#
#
if [ "$AFL_ON" -eq "0" ]; then
 echo "AFL compilation: disabled"
 LCC=${ACC}
 LCXX=${ACXX}

else
 echo "AFL compilation: enabled"
 if [ "$USE_GCC" -eq "0" ]; then
  LCC=${AFL_HOME}/afl-clang-fast
  LCXX=${AFL_HOME}/afl-clang-fast++
  #LCC=${AFL_HOME}/afl-clang
  #LCXX=${AFL_HOME}/afl-clang

 else
  LCC=${AFL_HOME}/afl-gcc
  LCXX=${AFL_HOME}/afl-g++
 fi
fi

#
# If you do not want ASan, make this empty
#
ASAN_BUILD="-fsanitize=address"
#ASAN_BUILD=""

#
# If you want to compile for x86-64, just leave empty
#
IA32_TARGET="-m32 -march=i686"
#IA32_TARGET=""

#
# Set these, hopefully, for CFLAGS and CXXFLAGS
#
# Note: 32-bit for ASan + AFL
#
if [ "$USE_GCC" -eq "0" ]; then
 LCFLAGS="${IA32_TARGET} -nopie -fno-stack-protector ${ASAN_BUILD}"
 LCXXFLAGS="${IA32_TARGET} -nopie -fno-stack-protector ${ASAN_BUILD}"
else
 LCFLAGS="${IA32_TARGET} -no-pie -fno-stack-protector ${ASAN_BUILD}"
 LCXXFLAGS="${IA32_TARGET} -no-pie -fno-stack-protector ${ASAN_BUILD}"
fi


#
# Set for any ./configure script options --prefix is done
# more in the build.sh of the application itself instead of
# at this level.
#
CONFIGFLAGS=""
