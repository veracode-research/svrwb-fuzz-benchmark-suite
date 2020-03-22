#!/bin/bash

SRCDIR=libarchive+81ce2c24f9fec640740de9bcea920ab71ef89059

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

LocCFLAGS="${LCFLAGS} -Wno-unused-function -Wno-error=unused-command-line-argument -Wno-error=deprecated-declarations"
LocCXXFLAGS="${LCXXFLAGS} -Wno-error=unused-command-line-argument -Wno-error=deprecated-declarations"

pushd ${SRCDIR}
/bin/sh build/autogen.sh
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LocCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LocCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LocCFLAGS}" make install

popd


