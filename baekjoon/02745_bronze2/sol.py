import sys
sys.stdin = open('input.txt')

N, B = input().split()
N = N[::-1]
B = int(B)
answer = 0

for i in range(len(N)):
    if N[i] in [str(i) for i in range(10)]:
        answer += (B ** i) * int(N[i])
    else:
        answer += (B ** i) * (ord(N[i]) - ord('A') + 10)
print(answer)