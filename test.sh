#!/bin/bash

let COUNT=0
for i in {1..100}; do         
    COUNTI=$(curl -s "http://localhost/host" | grep flask1 | wc -l)    
    let "COUNT = $COUNT + $COUNTI"    
done;

echo $COUNT
