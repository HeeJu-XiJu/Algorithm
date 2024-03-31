import sys
sys.stdin = open('input.txt')

string = input()
special = 0
answer = ''
voca = []

for s in string:
    if s == '<':
        number = len(voca)
        for _ in range(number):
            answer += voca.pop()
        special = 1
        answer += s
    elif s == '>':
        special = 0
        answer += s
    elif special == 1:
        answer += s
    elif s == ' ' and special == 0:
        number = len(voca)
        for _ in range(number):
            answer += voca.pop()
        answer += ' '
    else:
        voca.append(s)

number = len(voca)
if number != 0:
    for _ in range(number):
        answer += voca.pop()

print(answer)