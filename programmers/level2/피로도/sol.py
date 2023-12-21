from itertools import permutations


def solution(k, dungeons):
    perlists = list(permutations([num for num in dungeons], len(dungeons)))
                     
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