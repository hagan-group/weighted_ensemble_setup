#!/bin/sh 
echo $PWD
cd $PWD
abcd="$(python $PWD/abc.py)"
echo $abcd > abcd.txt
