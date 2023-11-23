def solution(survey, choices):
    answer = ''
    mdict = {}
    for i in 'RTCFJMAN':
        mdict[i] =0
        
    for num in range(len(survey)):
        mdict[survey[num][0]] += 4 - choices[num]
    
    if mdict['R'] >= mdict['T']:
        answer += 'R'
    else:
        answer += 'T'

    if mdict['C'] >= mdict['F']:
        answer += 'C'
    else:
        answer += 'F'

    if mdict['J'] >= mdict['M']:
        answer += 'J'
    else:
        answer += 'M'

    if mdict['A'] >= mdict['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))