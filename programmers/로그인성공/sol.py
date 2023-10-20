def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                break
        else:
            answer = 'fail'
        
    return answer

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))