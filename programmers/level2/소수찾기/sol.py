from itertools import permutations

def solution(numbers):
    # numbers로 만든 모든 숫자
    comb_list = []
    for num in range(1, len(numbers)+1):
        for comp in list(permutations(numbers, num)):
            comb_list.append(int(''.join(comp)))
    comb_list = list(set(comb_list))
    
    # 소수찾기
    answer = 0
    for comp in comb_list:
        count = 0
        if comp >= 2:
            # 에스토스테네스체
            for num in range(2, int(comp ** (1/2))+1):
                if comp % num == 0:
                    count += 1
                    break
            if count == 0:
                answer += 1
    
    return answer

print(solution("011"))


# 다른 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)