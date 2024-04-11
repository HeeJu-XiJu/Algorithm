import sys
sys.stdin = open('input.txt')

voca = input()
answer = []

for i in range(len(voca)):
    answer.append(voca[i:len(voca)])

answer = sorted(answer)

for a in answer:
    print(a)