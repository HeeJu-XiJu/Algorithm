# def solution(keymap, targets):
#     answer = []
#     for target in targets:
#         count = 0
#         for alp in target:
#             min_index = 200
#             for k in keymap:
#                 if alp in k and k.find(alp)+1 < min_index:
#                     min_index = k.find(alp)+1
#             count += min_index
#         if count == 200:
#             count = -1
#         answer.append(count)
#     return answer


def solution(keymap, targets):
    keydict = {}
    for key in keymap:
        for alp in key:
            if alp not in keydict.keys():
                keydict[alp] = key.find(alp)
            elif alp in keydict.keys() and keydict[alp] > key.find(alp):
                keydict[alp] = key.find(alp)

    answer = []
    for target in targets:
        answersum = 0
        for alp in target:
            if alp not in keydict.keys():
                answersum = -1
                break
            else:
                answersum += keydict[alp]+1
        answer.append(answersum)
    return answer
    

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(['AA'], ['B']))
print(solution(["BC"], ["AC", "BC"]))