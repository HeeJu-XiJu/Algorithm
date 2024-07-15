import sys
sys.stdin = open('input.txt')

N = int(input())
mlist = list(input().split(' '))

min_ans = ''
max_ans = ''

def check(i, j, k):
    if k == '>':
        return i > j
    else:
        return i < j

visited = [False] * 10

def solve(depth, s):
    global min_ans, max_ans
    if depth == N+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), mlist[depth-1]):
                visited[i] = True
                solve(depth+1, s+str(i))
                visited[i] = False

solve(0, '')
print(max_ans)
print(min_ans)