import itertools

def solution(babbling):
    perm1_list = ["aya", "ye", "woo", "ma"]
    perm2_list = []
    perm3_list = []
    perm4_list = []

    perm2 = itertools.permutations(perm1_list, 2)
    for i in list(perm2):
        a, b = i
        perm2_list.append(a+b)

    perm3 = itertools.permutations(perm1_list, 3)
    for i in list(perm3):
        a, b, c = i
        perm3_list.append(a+b+c)

    perm4 = itertools.permutations(perm1_list, 4)
    for i in list(perm4):
        a, b, c, d = i
        perm4_list.append(a+b+c+d)

    answer = 0

    for i in babbling:
        if i in perm1_list:
            answer += 1
        elif i in perm2_list:
            answer += 1
        elif i in perm3_list:
            answer += 1
        elif i in perm4_list:
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))