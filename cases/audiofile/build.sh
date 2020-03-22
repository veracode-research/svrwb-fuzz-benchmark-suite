#!/bin/bash

SRCDIR=audiofile-0.3.6

. ../config.sh

PREFX="--prefix=`pwd`/${SRCDIR}/install"

# XXX test for 32bit and use --host=x86 as a confgiure flag
LOCALCONFIGFLAGS="--disable-docs --disable-examples"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
if [ "$USE_GCC" -eq "0" ]; then
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX} ${LOCALCONFIGFLAGS}
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" make
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS}" FLAC_CFLAGS="${LCFLAGS}" make install
else
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS} -std=c++03" FLAC_CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX} ${LOCALCONFIGFLAGS}
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS} -std=c++03" FLAC_CFLAGS="${LCFLAGS}" make
  AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} CXXFLAGS="${LCXXFLAGS} -std=c++03" FLAC_CFLAGS="${LCFLAGS}" make install
fi
popd
