#!/bin/bash

echo "XXX: error: not really error, but you hardcoded your lib path"

SRCDIR=perl-5.21.7

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

tar xvf ${SRCDIR}.tar

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
echo "XXX FIX lddlflags"

if [ "$AFL_ON" -eq "0" ]; then
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 LD_LIBRARYPATH=$LD_LIBRARY_PATH:/home/arr/llvm-root/lib sh Configure   -Dafl_cc=${AFL_CC} -Dcc=${LCC}  -Accflags="${LCFLAGS}"   -de -Dusedevel -des -Aldflags="${LCFLAGS}" -Alddlflags="-shared -Wc,-fsanitize=address  -m32 -march=i686"
else
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 LD_LIBRARYPATH=$LD_LIBRARY_PATH:/home/arr/llvm-root/lib sh Configure   -Dafl_cc=${AFL_CC} -Dcc=${ACXX}  -Accflags="${LCFLAGS}"   -de -Dusedevel -des  -Aldflags=-fsanitize=address -Alddlflags="-shared  -m32 -march=i686"
fi

AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 make install DESTDIR=install
popd
