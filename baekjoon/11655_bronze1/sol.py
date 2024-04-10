import sys
sys.stdin = open('input.txt')

mlist = input()
answer = ''

for c in mlist:
    if 'A' <= c <= 'Z' and ord('A') <= ord(c) + 13 <= ord('Z'):
        answer += chr(ord(c) + 13)
    elif 'A' <= c <= 'Z' and ord('A') <= ord(c) + 13 - 26 <= ord('Z'):
        answer += chr(ord(c) + 13 - 26)
    elif 'a' <= c <= 'z' and ord('a') <= ord(c) + 13 <= ord('z'):
        answer += chr(ord(c) + 13)
    elif 'a' <= c <= 'z' and ord('a') <= ord(c) + 13 - 26 <= ord('z'):
        answer += chr(ord(c) + 13 - 26)
    elif '0' <= c <= '9' or ' ' == c:
        answer += c
    
print(answer)