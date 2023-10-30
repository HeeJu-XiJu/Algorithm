def solution(name, yearning, photo):
    answer = []
    count = 0
    for i in photo:
        for j in name:
            if j in i:
                count += yearning[name.index(j)]
        answer.append(count)
        count = 0
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))