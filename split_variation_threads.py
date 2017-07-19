#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:55:39 2017

@author: sdorai000
"""

#### ACTIVE EDIT ####

import sys
from threading import Thread
from threading import Lock
import time

result_count = 0
stairs = []

input_list = []
result_list = []

mutex = Lock()

def searchStairs(initial_stairs,n):

    #print("\nsearchString Invoked with initial_stairs and n:",initial_stairs,n)

    iteration_count = 0

    found_count = 0
    remaining_stairs = 0

    global mutex

    stairs = initial_stairs

    max_index = (n // 2 - 1) if n % 2 == 0 else (n // 2)

    while(True):

        iteration_count+=1

        #print("starting while:",stairs)

        if sum(stairs) == n:
            found_count+=1

            #mutex.acquire()
            #print("Found stairs:",stairs)
            #mutex.release()

            # check for exit from while
            if  stairs[1] == (n-max_index):
                break

            stairs.pop()

            if len(stairs) == 1:
                #print("Number of While iterations:", iteration_count)

                #print("Found Count:", found_count)

                # set found count
                mutex.acquire()
                result_list.append(found_count)
                mutex.release()

                return found_count

            max_possible_val = n - sum(stairs[:len(stairs)-1])
            next_max_val = (max_possible_val // 2 - 1) if max_possible_val % 2 == 0 else (max_possible_val // 2)

            if stairs[len(stairs)-1] + 1 <= next_max_val:
                stairs[len(stairs) - 1] += 1
            else:
                stairs[len(stairs) - 1] = max_possible_val

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

    #print("Number of While iterations:",iteration_count)

    #print("Found Count:",found_count)

    # set found count
    #mutex.acquire()
    result_list.append(found_count)
    #mutex.release()

    return found_count


def answer(n):

    iteration_count = 0

    total_count = 0
    remaining_stairs = 0

    stairs = []

    max_index = 0
    max_index = (n // 2 - 1) if n % 2 == 0 else (n // 2)

    threads = [None] * int(max_index)
    #threads = [None] * 1

    for i in range(1,max_index+1):
        stairs = []
        stairs.append(i)

        #total_count+=searchStairs(stairs,n)

        threads[i-1] = Thread(target=searchStairs, args=(stairs,n))
        threads[i-1].start()

    # join all threads
    for i in range(len(threads)):
        threads[i].join()

    print("Result list:",result_list)

    return sum(result_list)


def main(argv):
    # My code here

    brick_count = 150

    start = time.time()

    # run main function
    count = answer(brick_count)

    end = time.time()

    elapsed = end - start

    print("brick_count,result_count,elapsed_time:", count, result_count, elapsed)


if __name__ == "__main__":
    main(sys.argv)
