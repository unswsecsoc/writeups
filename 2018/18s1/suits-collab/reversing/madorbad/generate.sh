#!/bin/bash

python gen.py > bin.c
gcc bin.c -o bin
./bin $(cat flag)

