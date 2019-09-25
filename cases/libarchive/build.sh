#!/bin/bash

SRCDIR=libarchive

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

LocCFLAGS="${LCFLAGS} -Wno-unused-function -Wno-error=unused-command-line-argument -Wno-error=deprecated-declarations"
LocCXXFLAGS="${LCXXFLAGS} -Wno-error=unused-command-line-argument -Wno-error=deprecated-declarations"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
/bin/sh build/autogen.sh
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LocCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LocCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LocCFLAGS}" make install

popd


