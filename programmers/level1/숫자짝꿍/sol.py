# def solution(X, Y):
#     mlist = []

#     for i in X:
#         if i in Y:
#             mlist.append(i)
#             Y = Y.replace(str(i), 'a', 1)

#     if len(mlist):
#         answer = str(int(''.join(sorted(mlist, reverse=True))))
#     else:
#         answer = '-1'
#     print(Y)
#     return answer

def solution(X, Y):
    mlist = []

    for i in range(10):
        if str(i) in Y and str(i) in X: 
            mlist.append(str(i) * min(X.count(str(i)), Y.count(str(i))))

    if len(mlist):
        if int(sorted(mlist, reverse=True)[0]) == 0:
            answer = '0'
        else:
            answer = ''.join(sorted(mlist, reverse=True))
    else:
        answer = '-1'
        
    return answer


print(solution('100', '123450'))