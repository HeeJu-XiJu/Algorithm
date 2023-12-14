import heapq

def solution(operations):
    answer = []
    mlist = []
    for operation in operations:
        s, n = operation.split(' ')
        
        if s == 'I':
            heapq.heappush(mlist, int(n))
        elif len(mlist) > 0 and s == 'D' and n == '1':
            mlist.pop()
        elif len(mlist) > 0 and s == 'D' and n == '-1':
            heapq.heappop(mlist)
    
    if len(mlist) == 0:
        answer = [0, 0]
    else:
        answer.append(max(mlist))
        answer.append(min(mlist))

    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))


# 다른 풀이
import heapq as hq

def solution(operations):
    q = []
    q2 = []
    hq.heapify(q)
    hq.heapify(q2)

    for op in operations:
        if (op == 'D 1'):
            if q:
                while q:
                    hq.heappush(q2, -hq.heappop(q))
                hq.heappop(q2)
                while q2:
                    hq.heappush(q, -hq.heappop(q2))
        elif (op == 'D -1'):
            if q:
                hq.heappop(q)
        else:
            hq.heappush(q, int(op[2:]))

    return [max(q), min(q)] if q else [0, 0]