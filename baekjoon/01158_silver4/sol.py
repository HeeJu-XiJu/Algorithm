import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, sys.stdin.readline().split())

people = deque(i for i in range(1, n+1))
answer = '<'

while people:
    for _ in range(k-1):
        people.append(people.popleft())
    
    answer += str(people.popleft()) + ", "

answer = answer[:-2] + ">"

print(answer)