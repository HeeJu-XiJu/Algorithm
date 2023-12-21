from itertools import permutations


def solution(k, dungeons):
    perlists = list(permutations(dungeons, len(dungeons)))

    answer = -1
    for perlist in perlists:
        now = k
        count = 0
        for comp in perlist:
            if comp[0] <= now:
                now -= comp[1]
                count += 1
        if count > answer:
            answer = count

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))


# 다른 풀이
from itertools import permutations

def solution(k, d):
    for i in range(len(d), 1, -1):
        for j in permutations(d, i):
            k2 = k
            count = 0
            for n in j: 
                if k2 >= n[0]:
                    k2 -= n[1]
                    count += 1
                else:
                    break
            if count == len(j):
                return len(j)
    return 0