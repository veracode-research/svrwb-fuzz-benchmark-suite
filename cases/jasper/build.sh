#!/bin/bash


SRCDIR=jasper

. ../config.sh


PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make install
popd

