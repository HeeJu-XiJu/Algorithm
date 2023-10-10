import sys
sys.stdin = open('input.txt')

a, b = list(map(int,input().split()))
baguni = []

for baguni_number in range(1, a + 1):
    baguni.append(0)

for numbers in range(1, b + 1):
    x, y, z = list(map(int,input().split()))

    for baguni_number in range(x-1, y):
        baguni[baguni_number] = z

print(*baguni)

