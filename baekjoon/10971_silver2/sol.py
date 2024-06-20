import sys
sys.stdin = open('input.txt')

N = int(input())

pricelist = []
for i in range(N):
    mlist = list(map(int, input().split(' ')))
    pricelist.append(mlist)

visited = [0] * N
price = 0
minprice = 10000000

def dfs(depth, x):
    global price, minprice
    if depth == N - 1: # 종료 조건
        if pricelist[x][0]: 
            price += pricelist[x][0]
            if price < minprice: # 최소값 비교
                minprice = price
            price -= pricelist[x][0] 
        return
    for i in range(1, N):
        if visited[i] == 0 and pricelist[x][i]: # 방문 안한 도시 일떄
            visited[i] = 1 # 방문 체크
            price += pricelist[x][i] # 방문 비용 합치기
            dfs(depth + 1, i) # 재귀
            visited[i] = 0 # 재귀가 끝나면 초기화
            price -= pricelist[x][i] # 재귀가 끝나면 초기화


dfs(0, 0)
print(minprice)