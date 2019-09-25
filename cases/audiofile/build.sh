#!/bin/bash

SRCDIR=audiofile

. ../config.sh


PREFX="--prefix=`pwd`/${SRCDIR}/install"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX} --disable-docs --disable-examples
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" make install
popd
