from queue import Queue

def solution(priorities, location):
    que = Queue()
    for idx, pri in enumerate(priorities):
        que.put((idx, pri))

    answer = []
    temp = 0
    while len(answer) < len(priorities):
        i = que.get()
        if temp == 0 or temp[1] < i[1]:
            temp = i
            que.put(i)
        elif i == temp:
            answer.append(i)
            temp = 0
        else :
            que.put(i)
    
    for idx in range(len(answer)):
        if answer[idx][0] == location:
            return idx+1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))


# 다른 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer