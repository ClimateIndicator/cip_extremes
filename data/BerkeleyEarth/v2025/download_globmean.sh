#!/bin/bash

# 01.06.2022

mkdir raw
pushd raw

file=Land_and_Ocean_summary.txt

if [ -f $file ]; then
   echo "raw/$file already exists - delete it manually to download new version"
else
    wget https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_summary.txt
fi

popd
