def solution(brown, yellow):
    for line in range(1, int(yellow ** (1/2))+1):
        row = int(yellow / line)
        if yellow % line == 0 and (line + 2) * (row + 2) == brown+yellow:
            return [row+2, line+2]

print(solution(24, 24))