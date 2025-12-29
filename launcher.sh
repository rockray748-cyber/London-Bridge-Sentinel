#!/bin/bash
cd ~/London-Bridge-Sentinel
while true; do
    # Run python silently and redirect all errors to a black hole
    python3 src/sentinel.py > /dev/null 2>&1
    sleep 10
done
