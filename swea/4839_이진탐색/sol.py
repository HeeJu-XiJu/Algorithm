import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # P : 전체페이지
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지
    P, A, B = map(int, input().split())

    # l 첫페이지, r 마지막페이지
    l = 1
    r = P
    count_A = 0
    while l != A and r != A:
        c = int((l+r)/2)
        if c < A:
            l = c
        else:
            r = c
        count_A += 1
    
    # m 첫페이지, s 마지막페이지
    m = 1
    s = P
    count_B = 0
    while m != B and s != B:
        c = int((m+s)/2)
        if c < B:
            m = c
        else:
            s = c
        count_B += 1

    if count_A > count_B:
        answer = 'B'
    elif count_A < count_B:
        answer = 'A'
    else:
        answer = 0

    print(f'#{tc} {answer}')
