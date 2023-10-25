def solution(s):
    dic = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
    }
    number = ''
    answer = ''
    for char in s:
        if char.isdigit() == True:
            answer += char
        else :
            number += char
        
        try : 
            answer += str(dic[number])
            number = ''
        except:
            pass

    answer = int(answer)

    return answer

print(solution("one4seveneight"))