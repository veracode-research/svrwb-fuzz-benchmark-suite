#!/bin/bash

SRCDIR=imageworsener-1.3.0

. ../config.sh


PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
scripts/autogen.sh
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make install
popd


