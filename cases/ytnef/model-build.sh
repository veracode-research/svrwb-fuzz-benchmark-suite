#!/bin/bash

SRCDIR=CHANGEME

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

LCFLAGS="-nopie -fno-stack-protector -fsanitize=address"
LCXXFLAGS="-nopie -fno-stack-protector -fsanitize=address"
LocCONFIGFLAGS="--prefix=`pwd`/$SRCDIR/install --with-gnu-ld "


pushd ${SRCDIR}
./autogen.sh
ac_cv_func_malloc_0_nonnull=yes AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" FLAC_CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${LocCONFIGFLAGS}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make install
popd


