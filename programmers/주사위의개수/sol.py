def solution(box, n):
    A, B, C = box
    row = A // n
    col = B // n
    height = C // n

    answer = row * col * height
    
    return answer


print(solution([10, 8, 6], 3))