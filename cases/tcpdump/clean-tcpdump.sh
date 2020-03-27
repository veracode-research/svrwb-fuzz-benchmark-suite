#!/bin/bash


P=(
  "tcpdump-4.9.0"
)

#  "tcpdump-4.9.1"

for A in "${P[@]}"
do
	pushd ${A}
	make clean
	make distclean
	rm -rf install
	popd
done
