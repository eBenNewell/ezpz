#!/usr/bin/env python3

a = "1.2.3"
b = "2.3.4"
c = "3.4.5"
d = "0.2.1"
e = "1.2.2"
nums = [a, b, c, d, e]


def solution(l):
    d = dict.fromkeys(l, 0)

    for v in l:
        # change the values at index, split them at '.' each. 
        d[v] = list(map(int, v.split('.')))

    d = sorted(d.items(), key=lambda x: x[1])

    return [i[0] for i in d]

print(solution(nums))