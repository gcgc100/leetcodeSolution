#!/bin/sh

error_exit() {
    echo $1 1>&2
    exit 1
}

if [ $1 == "-h" ]; then
    echo "bash initSolution.sh {seq} {url} {difficulty}"
fi

if [ $# == 3 ]; then
    NAME=$1-$(echo $2 | sed 's/.*problems\/\([^\/]*\)\/description.*/\1/')
    cp -R template solutions/$NAME || error_exit "copy template failed"
    cd $3 || error_exit "difficulty dir not found"
    
    ln -s ../solutions/$NAME .
    cd ..
fi
