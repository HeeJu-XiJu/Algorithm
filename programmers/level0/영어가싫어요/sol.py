def solution(numbers):
    number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = ''
    answer = ''
    for char in numbers:
        if number not in number_list:
            number += char
        else:
            answer += str(number_list.index(number))
            number = ''
            number += char
    answer += str(number_list.index(number))
    answer = int(answer)
            
    return answer

print(solution("onetwothreefourfivesixseveneightnine"))