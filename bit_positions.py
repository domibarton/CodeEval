#!/usr/bin/env python
import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        n, p1, p2 = [int(s) for s in l.split(',')]
        print str(n>>(p1-1)&1 == n>>(p2-1)&1).lower()