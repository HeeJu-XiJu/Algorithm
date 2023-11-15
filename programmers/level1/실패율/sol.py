# 실패율 = 클리어못한플레이어수 / 스테이지에 도달한 플레이어수

# def solution(N, stages):
#     mdict = {}
#     total = len(stages)
#     for i in range(1, N+1):
#         mdict[i] = stages.count(i) / total
#         total -= stages.count(i)

#     sortedmdict = dict(sorted(mdict.items(), key=lambda x: x[1], reverse=True))
#     answer = list(sortedmdict.keys())
#     return answer


def solution(N, stages):
    mdict = {}
    for i in range(1, N+2):
        mdict[i] = 0

    for i in stages:
        mdict[i] += 1

    total = len(stages)
    for i, j in mdict.items():
        if total != 0:
            mdict[i] = j / total
            total -= j
        else :
            mdict[i] = 0

    del(mdict[N+1])
    sortedmdict = dict(sorted(mdict.items(), key=lambda x: x[1], reverse=True))
    answer = list(sortedmdict.keys())
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))