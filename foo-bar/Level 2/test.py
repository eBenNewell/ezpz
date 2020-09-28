#!/usr/bin/env python3
la = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

def answer(l):
  
  d = dict.fromkeys(l, 0)
  for v in l:
    d[v] = list(map(int, v.split('.')))
    
  d = sorted(d.items(), key=lambda x: x[1])
  return [i[0] for i in d]

print(answer(la))