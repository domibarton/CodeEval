#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Dominique Barton
#
# This file is part of Dominique Barton's CodeEval solutions.
#
# Dominique Barton's CodeEval solutions are free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# Dominique Barton's CodeEval solutions are distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Dominique Barton's CodeEval solutions. If not, see
# <http://www.gnu.org/licenses/>.
#
"""
Solution for the CodeEval challenge "Bit Positions":
https://www.codeeval.com/open_challenges/19/
"""
import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        n, p1, p2 = [int(s) for s in l.split(',')]
        print(str(n >> (p1 - 1) & 1 == n >> (p2 - 1) & 1).lower())
