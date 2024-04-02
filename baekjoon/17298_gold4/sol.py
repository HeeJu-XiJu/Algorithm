import sys
sys.stdin = open('input.txt')

N = int(input())
lis = list(map(int,input().split()))
result = [-1] * N
stack = []
for i in range(N):
    while stack and lis[i]>lis[stack[-1]]:
        result[stack[-1]]=lis[i]
        stack.pop()
    stack.append(i)
print(*result)


# 시간초과 1
# import sys
# sys.stdin = open('input.txt')

# n = int(input())
# mlist = list(map(int, input().split(' ')))
# answer = []

# for s in range(n):
#     for r in range(s, n):
#         if mlist[s] < mlist[r]:
#             answer.append(str(mlist[r]))
#             break
#     if len(answer) < s+1:
#         answer.append(str(-1))

# print(' '.join(answer))

# 시간초과 2
# import sys
# from collections import deque
# sys.stdin = open('input.txt')

# n = int(input())
# mlist = deque(map(int, input().split(' ')))
# answer = []

# while mlist:
#     a = mlist.popleft()
#     for s in mlist:
#         if a < s:
#             answer.append(str(s))
#             break
#     if len(answer) + len(mlist) != n:
#         answer.append('-1')

# print(' '.join(answer))