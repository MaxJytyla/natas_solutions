#!/bin/bash

for i in $(seq 0 $num_scripts); let ni=$i+1; do py ./scripts/natas$(seq -f "%02g" $i $i).py; echo "natas$(seq -f "%02g" $i $i) is done. Password for natas$(seq -f "%02g" $ni $ni) is $(cat ./passwords/natas$ni)" done 