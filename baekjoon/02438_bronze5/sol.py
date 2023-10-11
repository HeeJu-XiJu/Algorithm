import sys
sys.stdin = open('input.txt')

for number in range(1, int(input())+1):
    print('*' * number)