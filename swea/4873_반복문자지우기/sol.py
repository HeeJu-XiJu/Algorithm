import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A = []
    for char in input():
        A.append(char)
    
    i = 0
    while i < len(A)-1:
        if A[i] == A[i+1]:
            # A.remove(A[i])
            # A.remove(A[i])
            A.pop(i)
            A.pop(i)
            i = 0
        else :
            i += 1
    
    answer = len(A)

    print(f'#{tc} {answer}')