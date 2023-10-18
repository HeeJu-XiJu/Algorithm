def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom3 = denom1 * denom2
    numer3 = (numer1 * denom2) + (numer2 * denom1)

    for i in range(1, denom3 + 1):
        if denom3 % i == 0 and numer3 % i == 0:
            denom3 /= i
            numer3 /= i
    
    answer.append(numer3)
    answer.append(denom3)

    return answer

print(solution(1, 2, 3, 4))