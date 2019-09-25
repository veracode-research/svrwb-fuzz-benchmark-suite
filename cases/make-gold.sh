#!/bin/bash

#
# link the best choices to bugs.json and the name of the app dir
#
pushd $1
ln -s bugs-${2}.json bugs.json
ln -s ${2} ${1}
popd
