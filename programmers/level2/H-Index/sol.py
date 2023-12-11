def solution(citations):
    h = 0 # 문제상 h
    count = 0 # h 이상이 몇 편인지
    n = len(citations)
    h_list = []
    while h <= n:
        for citation in citations:
            if citation >= h:
                count += 1
        if count >= h:
            h_list.append(h)
        elif count < h:
            break
        h += 1
        count = 0
    return max(h_list)


print(solution([3, 0, 6, 1, 5]))
print(solution([6, 6, 6, 6, 6]))
print(solution([0, 0, 0, 0, 0]))
print(solution([6, 5, 3, 3, 0]))


# 다른 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
