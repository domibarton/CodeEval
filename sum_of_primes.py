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
Solution for the CodeEval challenge "Sum Of Primes":
https://www.codeeval.com/open_challenges/4/
'''


def generate_primes():
    '''
    Returns a generator which generates infinite number of prime numbers.

    The generator is based on the Sieve of Eratosthenes, with the exception
    that we're going to build an infinite amount of prime numbers. Therefore
    we're not going to build "all" composites at once. Instead of it, we're
    only building the next upcoming composites in each loop.
    '''

    # This is our composite dict, where we store future composites.
    # Key is the composite, value is a list of "multipliers".
    c = {}

    # This is our number / counter.
    n = 2

    # Endless loop, because we're working as a generator.
    while True:

        # If number is not in composite dict, it's a prime. Therefore yield it
        # and add a new composite to our dict, which is the multiply of our
        # prime number.
        if n not in c:
            yield n
            c[n * 2] = [n]

        # If number is in composite dict, it's not a prime. Now things get a
        # bit tricky. I'll try to explain them below.
        else:
            # First of all get the list of "past" multipliers which led to this
            # composite and loop through them.
            for m in c[n]:
                # Because the current number (n) is a composite, we need to
                # calculate all "future" composites for each existing
                # multiplier (m). This basically means that we sum up the
                # current number (n) with the multiplier (m).
                #
                # For example, let's say:
                #
                #   the current number (n) is 10
                #
                #   then the multipliers (m) are 2 and 5
                #
                #   therefore future composites are
                #       12 (multiply of 2, i.e. 10 + 2)
                #       15 (multiply of 5, i.e. 10 + 5)
                #
                # We also need to do some exception handling, because the
                # composite (list) can be existing or not. In case the "future"
                # composite already exists, we need to update it's list. If it
                # isn't existing, we need to create a new list. Of course we
                # could check for an existing key, but it's much nicer to just
                # catch the KeyError exception when we try to access the dict
                # item.
                try:
                    c[n + m].append(m)
                except KeyError:
                    c[n + m] = [m]

            # Last but not least, delete the current composite because it's no
            # longer required and we want a memory-efficient algorithm.
            del c[n]

        n += 1

if __name__ == '__main__':

    # Our counter (i) and our sum (s).
    i = 0
    s = 0

    # Start looping through prime number generator.
    for n in generate_primes():
        # Add prime number (n) to sum (s) and increase counter (i).
        s += n
        i += 1

        # We're in an "endless" generator loop, so we need to abort manually!
        if i >= 1000:
            break

    # Print sum (s).
    print(s)
