#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:55:39 2017

@author: sdorai000
"""


#### ACTIVE EDIT ####

import sys
import time

result_count=0
recursive_calls = 1
stairs=[]
total_bricks = 10

input_list=[]
result_list=[]


def printStuff(log):
    # print("in print stuff, log is:",log)
    enabled = False

    if enabled == True:
        print("RC:" + str(recursive_calls) + ":" + log)


def split(remaining_bricks, last_index, first_level=False):
    # variable initialization
    global result_count
    global stairs
    global recursive_calls
    global total_bricks

    invoke_split = False

    # logic start
    printStuff("29. first_level:" + str(first_level))

    # if not in the first level then use remaining bricks to update the find count
    if (first_level == False):
        stairs.append(remaining_bricks)
        result_count += 1

        print(">>>>>>>>>>>>>>>>>>>>>> 25. Found stairs:" + str(stairs))

        stairs.pop()

    # get the max range to search for any level
    if remaining_bricks % 2 == 0:
        max_index = remaining_bricks // 2 - 1
    else:
        max_index = remaining_bricks // 2

        # set start index
    start_index = last_index + 1

    # if nothing to loop over
    if len(stairs) > 0:
        if start_index <= last_index or start_index > max_index:
            printStuff("36. Last Index:" + str(last_index))
            printStuff("37. Popping and returning since loop does not converge")
            printStuff("38. Before pop stairs:" + str(stairs))

            return

    printStuff("45. Range of loop is start_idx,max_index:" + str(start_index) + "," + str(max_index))

    for i in range(start_index, max_index+1):

        invoke_split = False

        printStuff("50. i:" + str(i))
        printStuff("51. stairs:" + str(stairs))
        printStuff("52. result_count:" + str(result_count))
        printStuff("53. stairs,len(stairs)  :" + str(stairs) + "," + str(len(stairs)))

        new_remaining_bricks = 0

        if first_level == True:

            # just add and split for first level if it makes sense since we need at least 2 stairs
            stairs.append(i)

            new_remaining_bricks = total_bricks - sum(stairs)

            invoke_split = True

        else:

            printStuff("71. stairs:" + str(stairs))

            if (remaining_bricks - i) > i:

                stairs.append(i)

                new_remaining_bricks = total_bricks - sum(stairs)

                if (new_remaining_bricks > i):
                    invoke_split = True

        printStuff("78. Before split - stairs - first_time = True - stairs:" + str(stairs))
        printStuff("\n********************\n81. Invoking split - remaining_bricks,last_index:" +\
                   str(new_remaining_bricks) + "," + "," + str(i))

        recursive_calls += 1

        # invoke split
        split(new_remaining_bricks, i)

        stairs.pop()

        recursive_calls -= 1

        printStuff("\n********************\n89. Returning from split - i, start_index,max_index,remaining_bricks:" +\
                   str(i) + "," + str(start_index) + "," + str(max_index) + "," + str(remaining_bricks))


def main(argv):
    # My code here

    total_bricks = 10

    start = time.time()

    # run main function
    split(total_bricks, 0, first_level=True)

    end = time.time()

    elapsed = end - start

    print("total_bricks,result_count,elapsed_time:",total_bricks,result_count,elapsed)

if __name__ == "__main__":
    main(sys.argv)
