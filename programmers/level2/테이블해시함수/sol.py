def solution(data, col, row_begin, row_end):
    mdata = sorted(data, key=lambda x : [x[col-1], -x[0]])

    answer = 0
    for i in range(row_begin-1, row_end):
        temp = 0
        for j in range(len(mdata[0])):
                temp += mdata[i][j] % (i+1)
        answer = answer ^ temp
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))