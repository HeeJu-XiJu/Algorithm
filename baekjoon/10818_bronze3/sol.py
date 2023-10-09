import sys
sys.stdin = open('input.txt')

T = int(input())
my_list = list(map(int,input().split()))

my_max = max(my_list)
my_min = min(my_list)

print(my_min, my_max)