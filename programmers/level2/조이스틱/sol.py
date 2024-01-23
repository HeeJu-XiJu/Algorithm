def solution(name):
    # 조이스틱 위아래 횟수 구하기
    alpdiff = []
    for alp in name:
        alpdiff.append(min(ord(alp) - ord('A'), (ord('Z')+1 - ord(alp))))
    # alpdiff = [9, 0, 1]

    answer = sum(alpdiff)

    # 조이스틱 왼쪽오른쪽 횟수 구하기
    min_move = len(name) - 1
    # 오른쪽으로 쭉 갈 때, 오른쪽으로 갔다가 왼쪽으로 돌아갈 때 비교, 왼쪽으로 가다가 오른쪽으로 돌아올때 비교
    for i, _ in enumerate(alpdiff):
        next = i + 1
        while next < len(alpdiff) and alpdiff[next] == 0:
            next += 1
        
        min_move = min(min_move, i + i + (len(alpdiff) - next), i + (len(alpdiff) - next) * 2)
    answer += min_move
    return answer

print(solution("JAN"))


# 다른 풀이
def solution(name):
    # 조이스틱 위아래 횟수 구하기
    alpdiff = []
    for alp in name:
        alpdiff.append(min(ord(alp) - ord('A'), (ord('Z')+1 - ord(alp))))
    # alpdiff = [9, 0, 1]
        
    answer = sum(alpdiff)
        
    # 조이스틱 왼쪽오른쪽 횟수 구하기
    n = len(alpdiff)
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (alpdiff[next_idx] == 0):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)
    answer += move
    return answer