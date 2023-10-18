def solution(numer1, denom1, numer2, denom2):
    denom3 = denom1 * denom2
    numer3 = (numer1 * denom2) + (numer2 * denom1)

    for number in range(1, denom3 + 1):
        if denom3 % number == 0 and numer3 % number == 0:
            larger = number
        answer = [(numer3 / larger), (denom3 / larger)]

    return answer

print (solution(9, 2, 1, 3))