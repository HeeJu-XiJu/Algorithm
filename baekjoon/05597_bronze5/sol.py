import sys
sys.stdin = open('input.txt')

my_list = []

for number in range(1, 29):
    my_list += list(map(int,input().split()))

for answer in range(1, 31):
    if answer not in my_list:
        print(answer)