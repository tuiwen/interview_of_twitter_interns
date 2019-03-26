#!/bin/bash

cnt=0
wall=($1*10000)
while [[ cnt -lt $wall ]]; do
    echo "$((RANDOM%20+2000))-$((RANDOM%12+1))-$((RANDOM%31+1)) $((RANDOM%24+1)):$((RANDOM%60+1)):$((RANDOM%60+1))"
    ((cnt++))
done
