# BFS 구현 실패
def solution(tickets):
    tickets.sort()
    visited = []
    answer = ['ICN']

    def BFS(tickets, airline):
        for ticket in tickets:
            if len(answer) == len(tickets)+1:
                break
            start, end = ticket
            if ticket not in visited and start == airline:
                visited.append(ticket)
                answer.append(end)
                BFS(tickets, end)

    BFS(tickets, 'ICN')
    return answer


# deque 활용 BFS
from collections import deque

def solution(tickets):
    tickets.sort()
    q = deque()
    q.append(['ICN', ['ICN'], []])

    while q:
        start, answer, visited = q.popleft()
        if len(visited) == len(tickets):
            return answer
        
        for ticket in tickets:
            if ticket not in visited and start == ticket[0]:
                q.append([ticket[1], answer+[ticket[1]], visited+[ticket]])


# tickets를 정렬했는데 answer를 한번더 정렬해야 함 왜지?
from collections import deque

def solution(tickets):
    tickets.sort()
    q = deque()
    q.append(['ICN', ['ICN'], []])
    visit = []

    while q:
        start, answer, visited = q.popleft()
        if len(visited) == len(tickets):
            visit.append(answer)
        
        for idx, ticket in enumerate(tickets):
            if idx not in visited and start == ticket[0]:
                q.append([ticket[1], answer+[ticket[1]], visited+[idx]])
    visit.sort()
    return visit[0]
    

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))