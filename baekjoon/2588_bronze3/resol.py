import sys
sys.stdin = open('input.txt')

char1 = int(input())
char2 = input()

print(char1 * int(char2[-1]))
print(char1 * int(char2[-2]))
print(char1 * int(char2[-3]))
print(char1 * int(char2))