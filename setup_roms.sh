#!/usr/bin/bash

if [[ $# -ne 2 ]]; then
    echo -e "Usage: $0 <WHAT> <TO>"
    exit 1
fi

WHAT=$1
TO=$2

find . -name "$WHAT" |
while read item; do
    echo -e "Found: $item"
    if echo $item | grep "\.zip"; then
        unzip "$item" -d $TO
        rm "$item"
    else
        mv "$item" $TO
    fi
done
