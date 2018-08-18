#!/bin/zsh

# [detail]
#   l   detailed info
#   S   sort file by size 
#   h   human-readable (K,M,G etc.)
#   M   not including (M) (then it [may] less than 1M)
ls -lSh * | grep -v M
