#!/bin/bash

SRCDIR=wavpack-5.0.0

. ../config.sh

if [ -z "${IA32_TARGET}" ];
then
	HOSTARCH=""
else
	HOSTARCH="--host=x86"
fi
PREFX="--prefix=`pwd`/${SRCDIR}/install ${HOSTARCH}"

mkdir ${SRCDIR}/install

pushd ${SRCDIR}
./autogen.sh
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CFLAGS="${LCFLAGS}" CXX=${LCXX} FLAC_CFLAGS="$LCFLAGS" ./configure ${CONFIGFLAGS} ${PREFX}
 
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make install
popd


