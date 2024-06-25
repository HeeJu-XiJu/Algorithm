import sys
sys.stdin = open('input.txt')

L, C = map(int, input().split(' '))
mlist = list(input().split(' '))
mlist.sort()

def dfs(depth, idx):
    if depth == L:
        vowel_count = 0
        consonant_count = 0
        for i in answer:
            if i in 'aeiou':
                consonant_count += 1
            else:
                vowel_count += 1
        if vowel_count >= 2 and consonant_count >= 1:
            print(''.join(answer))
            return
    for i in range(idx, C):
        if mlist[i] not in answer:
            answer.append(mlist[i])
            dfs(depth+1, i+1)
            answer.pop()

answer = []
dfs(0, 0)