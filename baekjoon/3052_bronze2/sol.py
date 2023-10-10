import sys
sys.stdin = open('input.txt')

my_list = []

for number in range(1, 11):
    a = int(input())
    n = a % 42
    if n not in my_list:
        my_list.append(n)

print(len(my_list))
