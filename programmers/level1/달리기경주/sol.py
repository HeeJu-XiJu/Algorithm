# def solution(players, callings):
#     answer = players
#     for i in callings:
#         before_num = answer.index(i)-1
#         before = answer[before_num]
#         answer[before_num+1] = before
#         answer[before_num] = i
#     return answer

# def solution(players, callings):
#     mlist = players
#     for i in callings:
#         answer = []
#         for j in range(len(mlist)):
#             if i == mlist[j]:
#                 answer.pop()
#                 answer.append(mlist[j])
#                 answer.append(mlist[j-1])
#             else:
#                 answer.append(mlist[j])
#         mlist = answer
#     return mlist


# def solution(players, callings):
#     answer = players
#     for i in callings:
#         num = players.index(i)
#         answer.remove(i)
#         answer.insert(num-1, i)
#     return answer


# def solution(players, callings):
#     mdict = {}
#     answer = players
#     for i in callings:
#         mdict[i] = mdict.get(i, 0) + 1
    
#     for i, j in mdict.items():
#         while j != 0:
#             num = players.index(i)
#             answer.remove(i)
#             answer.insert(num-1, i)
#             j -= 1
#     return answer


def solution(players, callings):
    # i 등수 j 선수이름 
    numdict = {}
    for i, j in enumerate(players):
        numdict[i] = j

    playersdict = {}
    for i, j in enumerate(players):
        playersdict[j] = i

    for j in callings:
        # 호명된 선수 등수
        num1 = playersdict[j]
        # 앞선수 등수
        num2 = num1 - 1
        # 추월하기전 앞선수 이름
        before = numdict[num2]

        # 추월 후
        numdict[num1]=before
        numdict[num2]=j

        playersdict[j] = num2
        playersdict[before] = num1
    
    answer = list(numdict.values())
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))