#!/usr/bin/env python3

a = "1.2.3"
b = "2.3.4"
c = "3.4.5"
d = "0.2.1"
e = "1.2.2"
nums = [a, b, c, d, e]

def solution(l):
    
    # Creates a new dictionary but with keys and values added. 
    # from keys being our list that we provided up above
    # the values being 0 here as you can see. This was set but will change. 
    d = dict.fromkeys(l, 0)
    # I have a key value store now that d has been created. 
    print(d)
    print("Just finished creating the key value store")
    # Check your values with a for loop
    for v in l:
        print("During the function in the for loop")
        print(v)
        # change the values at index, split them at '.' each. 
        # 
        # Here just take my value in the key value store at index v 
        # and split it. 
        d[v] = list(map(int, v.split('.')))
        print(d[v])
        print()
    # sort the list here without any side effects using lambda        
    a = d.items()
    print(a)
    print("\n")
    d = sorted(d.items(), key=lambda x: x[1])

    print(d)
    # print index 0 here otherwise 1 will be the value and 2 will return tuple index out of rnage
    return [i[0] for i in d]

print("After the function")
print(solution(nums))