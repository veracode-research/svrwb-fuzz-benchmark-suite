#!/bin/bash

P=(
  "audiofile"
  "imageworsener"
  "jasper"
  "lame"
  "libarchive"
  "perl"
  "sqlite"
  "tcpdump"
  "wavpack"
  "ytnef"
)

for p in "${P[@]}"
do
	echo $p
	pushd $p
	/bin/bash clean.sh
	popd
done

# Excess
rm -rf  audiofile/audiofile-0.3.6/[config.h].in  \
        imageworsener/imageworsener-1.3.0/Makefile  \
        imageworsener/imageworsener-1.3.0/autom4te.cache/output.2   \
        imageworsener/imageworsener-1.3.0/autom4te.cache/traces.2   \
        imageworsener/imageworsener-1.3.0/config.h   \
        imageworsener/imageworsener-1.3.0/config.log   \
        imageworsener/imageworsener-1.3.0/config.status   \
        imageworsener/imageworsener-1.3.0/libtool   \
        imageworsener/imageworsener-1.3.0/src/.deps/   \
        imageworsener/imageworsener-1.3.0/stamp-h1   \
        jasper/jasper-1.701.0/data/Makefile.in   \
        libarchive/libarchive+81ce2c24f9fec640740de9bcea920ab71ef89059/autom4te.cache/   \
        perl/perl-5.21.7/.config/   \
        perl/perl-5.21.7/UU/   \
        perl/perl-5.21.7/config.sh.old   \
        perl/perl-5.21.7/try.c   \
        wavpack/wavpack-5.0.0/Makefile   \
        wavpack/wavpack-5.0.0/autom4te.cache/output.2   \
        wavpack/wavpack-5.0.0/autom4te.cache/traces.2   \
        wavpack/wavpack-5.0.0/cli/.deps/   \
        wavpack/wavpack-5.0.0/cli/.libs/   \
        wavpack/wavpack-5.0.0/cli/Makefile   \
        wavpack/wavpack-5.0.0/config.log   \
        wavpack/wavpack-5.0.0/config.status   \
        wavpack/wavpack-5.0.0/include/Makefile   \
        wavpack/wavpack-5.0.0/libtool   \
        wavpack/wavpack-5.0.0/man/Makefile   \
        wavpack/wavpack-5.0.0/src/Makefile   \
        wavpack/wavpack-5.0.0/wavpack.pc   \
        ytnef/ytnef-1.9.2/autom4te.cache/output.3   \
        ytnef/ytnef-1.9.2/autom4te.cache/traces.3   
