"""
Compute next permutation of P

Run doctest: python -m doctest -v next_permutation.py
"""

def next_permutation(p):
    n = len(p)
    found = False
    for i in range(n-2, -1, -1):
        if p[i] < p[i+1]:
            found = True
            break
    if not found:
        return reversed(p)
    for j in range(n-1, i, -1):
        if p[j] > p[i]:
            break
    p[i], p[j] = p[j], p[i]
    p[i+1:] = reversed(p[i+1:])
    return p
