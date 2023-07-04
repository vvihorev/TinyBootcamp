from __future__ import division
 
from bisect import bisect
 
def decompose(k, t, n):
    pown = [i ** 5 for i in range(t)]
    pvals = set(pown)
    def find(k, t, n, data):
        t5 = bisect(pown, t) - 1
        tn5 = bisect(pown, t/n) - 1
        if n == 2:
            for v in range(tn5, t5+1):
                if data and v > data[-1]:
                    continue
                w = t - pown[v]
                w5 = bisect(pown, w) - 1
                if pown[w5] + pown[v] == t:
                    print("--", data, v, w5)
        else:
            for s in range(t5, tn5 - 1, -1):
                u = t - pown[s]
                if data and data[-1] < s:
                    continue
                find(k, u, n - 1, data + [s])
    find(5, t ** 5, n, [])
             
         
for i in range(5, 145):
    decompose(5, i, 4)
