def solution(s):
    mlist = list(map(int, s.split()))
    answer = f'{min(mlist)} {max(mlist)}'
    return answer

print(solution("1 2 3 4"))