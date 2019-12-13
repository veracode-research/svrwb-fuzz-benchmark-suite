#!/bin/bash

SRCDIR=audiofile-0.3.6

. ../config.sh


PREFX="--prefix=`pwd`/${SRCDIR}/install"
LOCALCONFIGFLAGS="--disable-docs --disable-examples"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX} ${LOCALCONFIGFLAGS}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" make install
popd
