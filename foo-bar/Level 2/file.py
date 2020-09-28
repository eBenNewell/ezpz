#!/usr/bin/env python3
goog_list = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
final = []
item_list = []
dick = {}

for item in goog_list:
#     item_list.append(item.split("."))
    for num in range(101):
        dick[num] = []
    try:
        print(item.split(".")[0], item.split(".")[1], item.split(".")[2])
    except:
        try:
            print(item.split(".")[0], item.split(".")[1])
        except:
            try:
                print(item.split(".")[0])
            except:
                pass
#     print(item.split(".")[1])
#     print(item.split(".")[2])

dick[num].append(item.split(".")[0])
