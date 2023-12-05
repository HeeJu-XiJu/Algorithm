def solution(lines):
    set1 = set(range(lines[0][0], lines[0][1]))
    set2 = set(range(lines[1][0], lines[1][1]))
    set3 = set(range(lines[2][0], lines[2][1]))
    
    answerset = set1 & set2 | set1 & set3 | set2 & set3

    return len(answerset)

print(solution([[4, 7], [4, 5], [6, 7]]))