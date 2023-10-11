import sys
sys.stdin = open('input.txt')

S = input()
answer_list = [-1] * 26

for char in S:
    if answer_list[ord(char)-97] == -1:
        answer_list[ord(char)-97] = S.index(char)

print(*answer_list)