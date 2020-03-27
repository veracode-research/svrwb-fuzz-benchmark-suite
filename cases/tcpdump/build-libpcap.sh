#!/bin/bash


PSRCDIR=libpcap

. ../config.sh

if [ -z "${IA32_TARGET}" ];
then
	HOSTARCH=""
else

	HOSTARCH="--target=x86 --host=x86"
fi

PREFX="--prefix=`pwd`/${PSRCDIR}/install ${HOSTARCH}"

mkdir ${PSRCDIR}/install

pushd ${PSRCDIR}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" ./configure ${CONFIGFLAGS} ${PREFX}
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make
AFL_CC=${ACC} AFL_CXX=${ACXX} CC=${LCC} CXX=${LCXX} CFLAGS="${LCFLAGS}" make install
popd

