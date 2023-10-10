import sys
sys.stdin = open('input.txt')

a, b = list(map(int,input().split()))
baguni = []

for numbers in range(1, a + 1):
    baguni.append(numbers)

for baguni_numbers in range(1, b + 1):
    x, y = list(map(int,input().split()))
    baguni[x-1], baguni[y-1] = baguni[y-1], baguni[x-1]

print(*baguni)