#!/bin/bash

SRCDIR=lame

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" ./configure ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" make install
popd

