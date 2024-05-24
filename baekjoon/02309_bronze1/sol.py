import sys
sys.stdin = open('input.txt')

mlist = []
for _ in range(9):
    mlist.append(int(input()))

mlist.sort()
msum = sum(mlist)

for i in range(8):
    if len(mlist) == 7:
        break
    for j in range(i+1, 9):
        if msum - mlist[i] - mlist[j] == 100:
            a = mlist[i]
            b = mlist[j]
            mlist.remove(a)
            mlist.remove(b)
            break

for i in range(7):
    print(mlist[i])