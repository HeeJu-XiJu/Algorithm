import sys
sys.stdin = open('input.txt')

a, b = list(map(int,input().split()))
my_list = []
reverse = 0

for baguni_set in range(1, a+1):
    my_list.append(baguni_set)

for change in range(b):
    i, j = list(map(int,input().split()))
    reverse = my_list[i-1:j]
    reverse.reverse()
    my_list[i-1:j] = reverse

print(*my_list)