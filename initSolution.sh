#!/bin/sh

if [ $# == 3 ]; then
    NAME=$1-$(echo $2 | sed 's/.*problems\/\([^\/]*\)\/description.*/\1/')
    cp -R template solutions/$NAME
    cd $3
    ln -s ../solutions/$NAME .
    cd ..
fi
