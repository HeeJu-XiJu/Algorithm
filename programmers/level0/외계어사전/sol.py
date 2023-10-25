def solution(spell, dic):
    answer = 2
    my_list = []
    for j in range(len(dic)):
        count = 0
        for i in range(len(spell)):
            if spell[i] in dic[j]:
                count += 1
        if count == len(spell):
            answer = 1

    return answer

print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))