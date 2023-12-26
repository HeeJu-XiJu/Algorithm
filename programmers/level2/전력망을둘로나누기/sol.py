# def solution(n, wires):
#     answer = 101
#     # num1(전력망 1개)씩 빼고 전력망 수 세아리기
#     for num1 in range(len(wires)):
#         searchdict = {}
#         # num1빼고 n-1번 반복
#         for num2 in range(1, n+1):
#             for wireidx in range(len(wires)):
#                 if num2 in wires[wireidx] and num1 != wireidx:
#                     searchdict[str(num2)] = searchdict.get(str(num2), 0) + 1
#         if answer > max(searchdict.values()) - min(searchdict.values()):
#             answer = max(searchdict.values()) - min(searchdict.values())
#     return answer

from collections import defaultdict

def solution(n, wires):
    answer = 101
    # 전체전력망 중 num1(전력망 1개)을 빼기 위한 for문
    for num1 in range(len(wires)):
        searchdict = defaultdict(list)
        for idx in range(len(wires)):
            if num1 != idx:
                # 전력망 연결관계 파악
                v1, v2 = wires[idx]
                if len(searchdict.keys()) == 0:
                    searchdict[v1].append(v2)
                else:
                    count = 0
                    for key in searchdict.keys():
                        if v1 in searchdict[key]:
                            searchdict[key].append(v2)
                            count +=1
                            break
                        elif v2 in searchdict[key]:
                            searchdict[key].append(v1)
                            count +=1
                            break
                    if count == 0:
                        searchdict[v1].append(v2)
        lenlist = []
        for value in searchdict.values():
            lenlist.append(len(value))
        if len(lenlist) >= 2 and answer > max(lenlist) - min(lenlist):
            answer = max(lenlist) - min(lenlist)
        elif len(lenlist) == 1 and answer > max(lenlist):
            answer = max(lenlist)
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))