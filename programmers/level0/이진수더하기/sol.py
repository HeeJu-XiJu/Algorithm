def solution(bin1, bin2):
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer

print(solution("10", "11"))