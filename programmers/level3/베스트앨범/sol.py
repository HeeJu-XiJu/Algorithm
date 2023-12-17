import heapq

def solution(genres, plays):
    # 장르순 찾기
    bestdict = {}
    for idx in range(len(plays)):
        bestdict[genres[idx]] = bestdict.get(genres[idx], 0) + plays[idx]
    
    bestdict = sorted(bestdict.items(), key=lambda x: x[1], reverse=True)

    # 장르순, 플레이순으로 나열
    answer = []
    for genre, _ in bestdict:
        temp = []
        for idx in range(len(plays)):
            if len(temp) < 2 and genres[idx] == genre:
                heapq.heappush(temp, (plays[idx], idx))
            elif len(temp) == 2 and genres[idx] == genre and plays[idx] > temp[0][0]:
                    heapq.heappop(temp)
                    heapq.heappush(temp, (plays[idx], idx))
        
        if len(temp) == 2 and temp[0][0] == temp[1][0] :
            for idx in range(len(temp)):
                answer.append(temp[idx][1])
        else:
            for idx in range(len(temp)-1, -1, -1):
                answer.append(temp[idx][1])
        
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", 'classic'], [500, 600, 150, 800, 2500, 800]))