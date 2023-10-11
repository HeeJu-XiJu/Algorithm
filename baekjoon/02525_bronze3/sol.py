import sys
sys.stdin = open('input.txt')

A, B = list(map(int,input().split()))
C = int(input())

result_H1 = A + (C // 60)
result_M1 = B + (C % 60)

if result_M1 >= 60:
    result_M2 = result_M1 - 60
    result_H2 = result_H1 + 1
else:
    result_M2 = result_M1
    result_H2 = result_H1

if result_H2 >= 24:
    result_H3 = result_H2 - 24
else:
    result_H3 = result_H2 


print(result_H3, result_M2)