def solution(n, arr1, arr2):
    mlist1 = []
    jinsu = ''
    for i in arr1: 21
        while i != 0:
            jinsu += str(i % 2)
            i = i // 2
        while len(jinsu) != n:
            jinsu = jinsu + '0'
        mlist1.append(jinsu[::-1])
        jinsu = ''
    
    mlist2 = []
    for i in arr2:
        while i != 0:
            jinsu += str(i % 2)
            i = i // 2
        while len(jinsu) != n:
            jinsu = jinsu + '0'
        mlist2.append(jinsu[::-1])
        jinsu = ''
    
    answer = []
    a = ''
    for i in range(n):
        for j in range(n):
            if mlist1[i][j] == '1' or mlist2[i][j] == '1':
                a += '#'
            else:
                a += ' '
        answer.append(a)
        a = ''
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))