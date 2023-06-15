#!/bin/bash
for inf in *.out
do
tac $inf | grep -m 1 "Thermal correction to Gibbs Free Energy" | tr '\n' ' '
echo $inf
done
