#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    # Check k
    # Start iterating at beginning
    max_and = 0
    starting_point = n
    i = starting_point
    largest_possible = k - 1
    max_reached = False
    while i > 1:
        j = i - 1
        while j > 0:
            iteration_and = j & i
#            print("{} {} {}".format(i, j, iteration_and))

            if iteration_and > max_and and iteration_and < k: 
                max_and = iteration_and
                if max_and == largest_possible: 
                    max_reached = True
                    break

            j -= 1

        if max_reached:
            break
        i -= 1
    print(max_and)    
