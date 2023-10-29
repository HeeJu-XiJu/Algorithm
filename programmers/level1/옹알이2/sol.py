def solution(babbling):
    # 1
    mlist1 = ["aya", "ye", "woo", "ma"]

    # 2
    mlist2 = []
    for i in mlist1:
        for j in mlist1:
            if i != j:
                mlist2.append(i+j)
                for k in mlist1:
                    if j != k:
                        mlist2.append(i+j+k)
                        for l in mlist1:
                            if k != l:
                                mlist2.append(i+j+k+l)
                                
    answer = 0
    for i in babbling:
        if i in mlist1 or i in mlist2:
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))