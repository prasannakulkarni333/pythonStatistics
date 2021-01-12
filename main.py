#!/usr/local/bin/python3
#!python3

import math

whatIsMean = 'Average - Sum / Count'

def mean(*args):
    cal_mean = sum(args)
    return cal_mean / len(args)

printf = mean(1, 2, 3)

print (printf)

