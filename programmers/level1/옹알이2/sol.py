def solution(babbling):
    # 1
    mlist = ["aya", "ye", "woo", "ma"]
                                
    answer = 0
    for i in babbling:
        for j in mlist:
            if j * 2 not in i:
                i = i.replace(j, str(mlist.index(j)))
        
        try :
            int(i)
            answer += 1
        except :
            pass

    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))