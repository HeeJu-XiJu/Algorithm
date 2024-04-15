import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())

GCB = 0
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        GCB = i
print(GCB)

LCB = 0
for i in range(1, min(a, b)+1):
    if (max(a, b) * i) % min(a, b) == 0:
        LCB = max(a, b) * i
        break
print(LCB)