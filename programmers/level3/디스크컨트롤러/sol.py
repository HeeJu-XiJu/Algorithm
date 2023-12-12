import heapq

def solution(jobs):
    finish = 0 # 현재 수행중인 프로세스가 끝나는 시간
    start = -1 # 현재 수행중인 프로세스가 시작한 시간
    wait = [] # 대기중인 프로세스
    time = 0 # 소요되는 시간
    count = 0 # 처리한 프로세스 수
    
    while len(jobs) > count:
        for job in jobs:
            if start < job[0] <= finish:
                heapq.heappush(wait, [job[1], job[0]])
        
        if len(wait) > 0:
            process = heapq.heappop(wait)
            start = finish
            finish = start + process[0]
            time += finish - process[1]
            count += 1
        else:
            finish += 1

    return int(time / count)

print(solution([[0, 3], [1, 9], [2, 6]]))