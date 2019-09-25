#!/bin/bash

#
# usage: best-version.sh app-root
#
# eg  best-version /path/to/cases/jasper
#
# This is a bit hokie, but the idea is to get different versions,
# build them, adjust the metadata files for running them, run them,
# then look at the uniqueness of bugs found
#
#

VERSIONS=(
	"tcpdump-4.9.0"
	"tcpdump-4.9.1"
)

LROOT=/home/arr/llvm-root
BMROOT=/home/arr/fuzz-benchmark-suite

GPD=${BMROOT}/util/gather_crash_data.py
UNI=${BMROOT}/util/check_bug_uniqueness_by_backtrace.py
UNIB=${BMROOT}/util/check_bug_uniqueness_by_backtrace_less_address.py
RESF=results-log.txt

pushd $1
for X in "${VERSIONS[@]}"
do
	#Fill out: download method here
	#git clone && git checkout rev
	# or
	#wget && tar zxvf
	# ...etc..


	cp model-build.sh build-${X}.sh
	cp model-bugs.json tmp-bugs.json


	#
	# modify build.sh and build.json to have the correct version 
	#
	perl -i.orig -p -e "s/^SRCDIR=CHANGEME$/SRCDIR=${X}/" build-${X}.sh
	repp=`printf '"apppath": "CHANGEME'`
	repq=`printf '"apppath": "%s' ${X}`
	perl -i.orig -p -e "s/${repp}\//${repq}\//g" tmp-bugs.json

	#
	# build this version
	#
	/bin/bash build-${X}.sh

	#
	# run and gather any crash dumps into bugs-version.json
	#
	PYTHONPATH=${LROOT}/lib/python3.7/site-packages:${BMROOT}/util python3  \
	    ${GPD} . tmp-bugs.json bugs-${X}.json

	#
	# check uniqueness with addresses
	#
	PYTHONPATH=${LROOT}/lib/python3.7/site-packages:${BMROOT}/util python3  \
	    ${UNI} bugs-${X}.json > results-${X}.txt

	#
	# check uniqueness w/o addresses
	#
	PYTHONPATH=${LROOT}/lib/python3.7/site-packages:${BMROOT}/util python3  \
	    ${UNIB} bugs-${X}.json > results-${X}-lessaddr.txt

	C=`grep 'unique:' results-${X}-lessaddr.txt | wc -l`
	echo ${C} ${X} >> ${RESF}

	#
	# Try and clean up some
	#
	rm tmp-bugs.json
	rm tmp-bugs.json.orig
	rm build-${X}.sh.orig	
done
popd
