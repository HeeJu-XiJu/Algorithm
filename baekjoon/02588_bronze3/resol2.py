import sys
sys.stdin = open('input.txt')

a = int(input())
b = int(input())
n = b

while n > 0:
    answer = a * (n % 10)
    n = n // 10
    print(answer)

print(a * b)