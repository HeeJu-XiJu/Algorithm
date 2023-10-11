import sys
sys.stdin = open('input.txt')

N = int(input())
my_list = list(map(int,input().split()))
my_max = max(my_list)
new_list = []

for number in range(N):
    values = (my_list[number]/my_max)*100
    new_list.append(values)

new_avg = sum(new_list) / len(new_list)
print(new_avg)