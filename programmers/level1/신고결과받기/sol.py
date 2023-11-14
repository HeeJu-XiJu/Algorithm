def solution(id_list, report, k):
    # 신고한사람 카운트
    answerdict = {}
    for i in id_list:
        answerdict[i] = 0

    # 신고한사람, 신고당한사람
    report = set(report)
    # 신고당한사람 : 신고당한 횟수
    countdict = {}
    for i in report:
        p1, p2 = i.split()
        countdict[p2] = countdict.get(p2, 0) + 1

    # 정지 대상
    xlist = []
    # 신고당한사람 : 신고당한 횟수    
    for i, j in countdict.items():
        if j >= k:
            xlist.append(i)
    
    # p1 신고한사람, p2 신고당한사람, x 정지대상
    for i in report:
        p1, p2 = i.split()
        for x in xlist:
            if x == p2:
                answerdict[p1] += 1

    answer = list(answerdict.values())
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))