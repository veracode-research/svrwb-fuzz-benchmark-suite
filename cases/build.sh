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
	/bin/bash build.sh
	popd
done
