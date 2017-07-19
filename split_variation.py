# version 0.82 seconds on n = 100

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:55:39 2017

@author: sdorai000
"""

#### ACTIVE EDIT ####

import sys
import time

result_count = 0
stairs = []

input_list = []
result_list = []

def answer(n):

    found_count = 0
    remaining_stairs = 0
    stairs = [1]

    max_index = (n // 2 - 1) if n % 2 == 0 else (n // 2)

    while(True):

        #print("starting while:",stairs)

        if sum(stairs) == n:
            found_count+=1

            #print("Found stairs:",stairs)

            # check for exit from while

            if stairs[0] == max_index and stairs[1] == (n-max_index):
                break

            stairs.pop()

            max_possible_val = n - sum(stairs[:len(stairs)-1])
            next_max_val = (max_possible_val // 2 - 1) if max_possible_val % 2 == 0 else (max_possible_val // 2)

            if stairs[len(stairs)-1] + 1 <= next_max_val:
                stairs[len(stairs) - 1] += 1
            else:
                stairs[len(stairs) - 1] = max_possible_val

            #stairs[len(stairs) - 1]+=1

            continue

        remaining_stairs = n - sum(stairs)

        if remaining_stairs > stairs[len(stairs)-1]:

            next_max_val = (remaining_stairs // 2 - 1) if remaining_stairs % 2 == 0 else (remaining_stairs // 2)

            if stairs[len(stairs)-1] + 1 <= next_max_val:
                stairs.append(stairs[len(stairs)-1] + 1)
            else:
                stairs.append(remaining_stairs)
        else:
            stairs[len(stairs)-1] += 1

    return found_count


def main(argv):
    # My code here

    brick_count = 100

    start = time.time()

    # run main function
    count = answer(brick_count)

    end = time.time()

    elapsed = end - start

    print("brick_count,result_count,elapsed_time:", count, result_count, elapsed)


if __name__ == "__main__":
    main(sys.argv)