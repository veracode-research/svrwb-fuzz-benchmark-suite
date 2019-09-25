#!/bin/bash


PSRCDIR=libpcap

. ../config.sh


PREFX="--prefix=`pwd`/${PSRCDIR}/install"

mkdir ${PSRCDIR}/install

pushd ${PSRCDIR}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make install
popd

