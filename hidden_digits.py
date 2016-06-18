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
Solution for the CodeEval challenge "Hidden Digits":
https://www.codeeval.com/open_challenges/122/
'''
import sys
import re
from string import maketrans

#
# Version 1: Using string translations (uses more memory).
#

t = maketrans(
    'abcdefghij',
    '0123456789'
)
r = re.compile(r'[^\d]')

with open(sys.argv[1], 'r') as f:
    for l in f:
        s = r.sub('', l.translate(t))
        print(s if s else 'NONE')

#
# Version 2: Using only regex and a mapping.
#

# m = {chr(i + 97): i for i in range(10)}
# r = re.compile(r'[^0-9a-j]')

# with open(sys.argv[1], 'r') as f:
#     for l in f:
#         s = r.sub('', l)
#         s = ''.join(map(lambda x: str(x) if x.isdigit() else str(m[x]), s))
#         print(s if s else 'NONE')
