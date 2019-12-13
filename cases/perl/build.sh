#!/bin/bash


SRCDIR=perl-5.21.7

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

tar xvf ${SRCDIR}.tar

mkdir ${SRCDIR}/install

pushd ${SRCDIR}

AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 LD_LIBRARYPATH=$LD_LIBRARY_PATH sh Configure   -Dafl_cc=${AFL_CC} -Dcc=${LCC}  -Accflags="${LCFLAGS}"   -de -Dusedevel -des -Aldflags="${LCFLAGS}" -Alddlflags="-shared -Wc,${ASAN_BUILD} ${IA32_TARGET}"

AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} ASAN_OPTIONS=detect_leaks=0 make install DESTDIR=install
popd
