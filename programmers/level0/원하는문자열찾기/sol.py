def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0

print(solution("AbCdEfG", "aBc"))