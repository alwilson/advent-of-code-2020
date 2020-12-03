#!/bin/bash -x

./convert_input.py
iverilog -o part2 part2.v counter200.v
time ./part2
rm input_hex.mem part2
