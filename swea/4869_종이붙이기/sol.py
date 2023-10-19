import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    paper = [1, 3, 5]
    N = int(int(input()) / 10)
    i = len(paper)
    while i < N :
        paper.append((paper[i-2] * 2) + paper[i-1])
        i += 1
    
    print(f'#{tc} {paper[N-1]}')