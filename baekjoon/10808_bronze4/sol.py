import sys
sys.stdin = open('input.txt')

string = input()
answer = [0] * 26

for s in string:
    answer[ord(s)-ord('a')] += 1

ans = ''
for a in answer:
    ans += str(a) + ' '

ans.strip()

print(ans)