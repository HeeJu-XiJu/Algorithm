import sys
sys.stdin = open('input.txt')
n = int(input())
result = 1

while n != 1 and n != 0:
    result *= n
    n -= 1

mresult = str(result).strip('0')
print(len(str(result)) - len(mresult))