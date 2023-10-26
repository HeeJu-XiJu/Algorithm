def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[(len(phone_number)-4):]
    return answer

# 다른 풀이
# 뒷자리 4개 phone_number[-4:]