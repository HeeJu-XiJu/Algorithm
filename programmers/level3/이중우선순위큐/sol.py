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