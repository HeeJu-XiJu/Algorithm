def solution(id_list, report, k):
    # 신고한사람 dict
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

    # p1 신고한사람, p2 신고당한사람
    for i in report:
        p1, p2 = i.split()
        if countdict[p2] >= k:
            answerdict[p1] += 1

    answer = list(answerdict.values())
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))