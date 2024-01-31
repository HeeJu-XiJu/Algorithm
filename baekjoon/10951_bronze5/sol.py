import sys
sys.stdin = open('input.txt')

while 1:
    try:
        a, b = list(map(int,input().split()))
        print(a + b)
    except:
        break