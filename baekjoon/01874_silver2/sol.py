import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

stack = []
printlist = []
numlist = []

for i in range(1, n+1):
    numlist.append(int(sys.stdin.readline()))

from collections import deque
numlist = deque(numlist)

for i in range(1, n+1):
    if len(stack) == 0 or stack[-1] != numlist[0]:
        stack.append(i)
        printlist.append('+')
    while len(stack) != 0 and stack[-1] == numlist[0]:
        stack.pop()
        printlist.append('-')
        numlist.popleft()

if len(stack) != 0:
    print('NO')
else:
    for str in printlist:
        print(str)