import sys
sys.stdin = open('input.txt')

n = int(input())
cal = input()
mdict = {}

for num in range(n):
    mdict[chr(65+num)] = input()

stack = []
for i in range(len(cal)):
    if cal[i] in ['+', '-', '*', '/']:
        str1 = stack.pop()
        str2 = stack.pop()
        if 'A' <= str1 <= 'Z':
            str1 = mdict[str1]
        if 'A' <= str2 <= 'Z':
            str2 = mdict[str2]
        stack.append(str(eval(str2 + cal[i] + str1)))
    else:
        stack.append(cal[i])
print('%.2f' %float(stack[0]))