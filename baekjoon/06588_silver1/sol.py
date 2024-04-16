import sys
sys.stdin = open('input.txt')

mlist = [True] * 1000001

for i in range(2, int(len(mlist) ** 0.5) + 1):
    if mlist[i]:
        for j in range(2 * i, 1000001, i):
            mlist[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for a in range(n-3, 2, -2):
        b = n - a
        if mlist[a] and mlist[b]:
            print(f'{n} = {b} + {a}')
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')