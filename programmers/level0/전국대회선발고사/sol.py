def solution(rank, attendance):
    for i in range(len(attendance)):
        if attendance[i] == False:
            rank[i] = max(rank)+1
    a, b, c = sorted(rank)[0:3]
    answer = 10000*rank.index(a) + 100*rank.index(b) + rank.index(c)

    return answer

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))
print(solution([1, 2, 3], [True, True, True]))