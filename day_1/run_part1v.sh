#!/bin/bash -x

./convert_input.py
iverilog -o part1 part1.v counter200.v
time ./part1
rm input_hex.mem part1
