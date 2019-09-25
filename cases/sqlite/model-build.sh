#!/bin/bash

SRCDIR=CHANGEME

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

#LocCONFIGFLAGS="--disable-amalgamation --disable-tcl ${PREFX}"
LocCONFIGFLAGS="--disable-tcl ${PREFX}"

mkdir ${SRCDIR}/install
mkdir build
pushd build
ASAN_OPTIONS=detect_leaks=0 AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ../${SRCDIR}/configure ${CONFIGFLAGS} ${LocCONFIGFLAGS}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ASAN_OPTIONS=detect_leaks=0 make sqlite3.c
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ASAN_OPTIONS=detect_leaks=0 make
make install
popd
