#!/bin/bash

#
# usage: prep_fuzz_disk.sh <mountlocation> <size>
#
#   
#
if [ "$#" -ne 2 ];
then
	printf "usage: prep_fuzz_disk.sh <mountloc> <size>\n"
	exit 0
fi
L=$1
S=$2

sudo mkdir ${L}
sudo mount -t tmpfs -o size=${S} tmpfs ${L}
sudo chown arr:arr  ${L}

