#!/usr/bin/env python3


num = 3
l = [1, 2, 3, 2, 2, 2]

def answer(data, n):
    # Check if its in range
    if len(data) in range(99):
        print("Success! Data is in range")
    else:
        print("Error")
        print("Data in list out of range. Or note that the code just quit at step.")
    list2 = []
    print("The number of times a number has to show up is " + str(n))
    for m in data:
        # Am looking for the m that shows up more than n times.
        #
        x = data.count(m) > n
        print(x)

answer(l, num)
