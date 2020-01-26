import random

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    # middle used below (in place of [v]) for clarity
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    if len(left) > k:    return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - len(middle))

def median(L):
    n = len(L)
    l = top_k(L, n / 2 + 1)
    return max(l)

