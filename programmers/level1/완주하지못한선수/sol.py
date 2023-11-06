# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     answer = participant[0]
#     return answer


def solution(participant, completion):
    hash = {}
    for i in participant:
        hash[i] = hash.get(i, 0) + 1
        
    for i in completion:
        hash[i] -= 1

    for i, j in hash.items():
        if j == 1:
            answer = i
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "mislav"]))

# 다른 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 다른 풀이(2)
def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    
    for i in range(len(completion)):
        if p[i] != c[i]:
            return p[i]
    
    return p[-1]