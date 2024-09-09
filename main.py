#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## main.py
## File description:
## blabla
##

import math
import sys

def first_method(n, k):
    a = 1
    xn = n
    if (k < 1 or k > 4):
        sys.exit(84)
    if (n < 1):
        sys.exit(84)
    while (a != 101):
        print(a, end=' ')
        print("%.2f" % xn)
        xn = k * xn * ((1000 - xn) / 1000)
        a = a + 1

def second_method(n, i1, i2):
    k = 1
    save = 0
    i = 0
    if (n == 0 or n < 0):
        sys.exit(84)
    if (i1 == 0 or i1 < 0):
        sys.exit(84)
    if (i2 == 0 or i2 <= i1 or i2 < 0):
        sys.exit(84)
    while (k <= 4):
        while (i <= i1):
            save = n
            n = (k * save) * ((1000 - save) / 1000)
            i = i + 1
        while (i <= i2 + 1):
            print("%.2f" % k, end=' ')
            print("%.2f" % n)
            save = n
            n = (k * save) * ((1000 - save) / 1000)
            i = i + 1
        k = k + 0.01
        i = 0

def checker():
    a = len(sys.argv)
    b = 1
    while (b < a):
        try:
            val = float(sys.argv[b])
        except ValueError:
            sys.exit(84)
        b = b + 1


def main(argv):
    if (len(sys.argv) < 3 or len(sys.argv) > 4 or sys.argv[1] == '-h'):
        sys.exit(84)
    checker()
    if (len(sys.argv) == 3):
        first_method(float(sys.argv[1]), float(sys.argv[2]))
    if (len(sys.argv) == 4):
        second_method(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
