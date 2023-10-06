import sys
sys.stdin = open('input.txt')

char = input()

if char.isalpha():
    if char.islower():
        answer = char.upper()
    else:
        answer = char.lower()
else:
    answer = char

print(f'{char}(ASCII: {ord(char)}) => {answer}(ASCII: {ord(answer)})')