def solution(s, n):
    answer = ''
    for char in s:
        if 65 <= ord(char) + n <= 90 : # 대문자 아스키코드 + n만큼
            answer += chr(ord(char) + n)
        elif ord(char) <= 90 and ord(char) + n >= 91 : # 대문자 아스키코드 Z보다 클 때
            answer += chr(ord(char) + n - 26)
        elif ord(char) >= 97 and ord(char) + n <= 122 : # 소문자 아스키코드 + n만큼
            answer += chr(ord(char) + n)
        elif ord(char) >= 97 and ord(char) + n >= 123 : # 소문자 아스키코드 z보다 클 때
            answer += chr(ord(char) + n - 26)
        elif char == ' ':
            answer += char
    return answer

print(solution("Z Bza", 1))