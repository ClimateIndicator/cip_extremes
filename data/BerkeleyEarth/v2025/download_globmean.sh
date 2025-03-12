#!/bin/bash

# 01.06.2022

mkdir raw
pushd raw
wget https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_summary.txt

popd
