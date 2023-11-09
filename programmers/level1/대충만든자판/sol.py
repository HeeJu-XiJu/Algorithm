def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for alp in target:
            min_index = 200
            for k in keymap:
                if alp in k and k.find(alp)+1 < min_index:
                    min_index = k.find(alp)+1
            count += min_index
        if count == 200:
            count = -1
        answer.append(count)
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))