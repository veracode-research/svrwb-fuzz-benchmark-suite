#!/bin/bash

# Currently this is not very nice for other people to use...and likely should
# ensure we have some consistency.
#
# linux disable ASLR:
#  sysctl kernel.randomize_va_space=0
# or echo to proc.
# change back to 1 or 2 after.
#

#gcc is -no-pie
#clang is -nopie for some versions

SRCDIR=libarchive-3.3.3
LCC=/home/areiter/llvm-root/bin/clang
LCXX=/home/areiter/llvm-root/bin/clang++
LCFLAGS="-nopie -fno-stack-protector -fsanitize=address -Wno-error=unused-command-line-argument -Wno-error=deprecated-declarations"
LCXXFLAGS="-nopie -fno-stack-protector -fsanitize=address -Wno-error=unused-command-line-argument -Wno-error=deprecated-declarations"
CONFIGFLAGS="--disable-examples --prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

cd $SRCDIR &&  \
  CC=$LCC CFLAGS=$LCFLAGS CXX=$LCXX CXXFLAGS=$LCXXFLAGS ./configure $CONFIGFLAGS &&  \
  make &&  \
  make install &&  \
  cd ..

# For OS X one can also use the following
#python ../../util/3rdparty/change_mach_o_flags.py --executable-heap --no-pie lame-3.99.5/frontend/lame

