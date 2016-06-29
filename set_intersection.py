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
'''
Solution for the CodeEval challenge "Set Intersection":
https://www.codeeval.com/open_challenges/30/
'''
import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        s1, s2 = l.strip().split(';')
        s1     = set(s1.split(','))
        s2     = set(s2.split(','))
        i      = sorted(s1 & s2)
        print(','.join(i))
