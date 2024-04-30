import sys
sys.stdin = open('input.txt')

N, B = map(int, input().split())
answer = ''

while N >= 1:
    a = N % B
    if a <= 9:
        answer += str(a)
    else:
        answer += chr(ord('A') + a - 10)
    N = N // B

print(answer[::-1])