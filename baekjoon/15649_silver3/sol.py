import sys
sys.stdin = open('input.txt')
from itertools import permutations

N, M = map(int, input().split(' '))

mlist = []
for i in range(1, N+1):
    mlist.append(i)

perm = list(permutations(mlist, M))

for list in perm:
    print(' '.join(map(str, list)))