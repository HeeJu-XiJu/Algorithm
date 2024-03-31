import sys
from collections import deque
sys.stdin = open('input.txt')

string = sys.stdin.readline()
special = 0
answer = ''
voca = deque()

for s in string:
    if s == '<':
        special = 1
        voca.append(s)
    elif s == '>':
        special = 0
        voca.append(s)
        answer += ''.join(voca)
        voca = deque()
    elif s == ' ':
        answer += ''.join(voca)
        answer += ' '
        voca = deque()
    elif special == 1:
        voca.append(s)
    else:
        voca.appendleft(s)

answer += ''.join(voca)
answer.strip()

print(answer)