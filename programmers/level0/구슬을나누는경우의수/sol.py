def solution(balls, share):
    if balls == share:
        answer = 1
    else:
        answer = 1
        for num in range(1, balls+1):
            answer *= num
        
        for num in range(1, share+1):
            answer /= num

        for num in range(1, (balls-share)+1):
            answer /= num

    return answer

print(solution(5, 3))