#!/usr/bin/env python3
goog_list = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
final = []
item_list = []
dick = {}

for item in goog_list:
    item_list.append(item.split("."))
for num in range(101):
    for i in range(0, len(goog_list) + 1):
        try:
            dick[num] = item_list[i][1]
        except:
            pass

print(dick)