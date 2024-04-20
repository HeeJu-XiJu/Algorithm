import sys
sys.stdin = open('input.txt')

num2 = int(input(), 2)
num8 = oct(num2)
print(num8[2:])