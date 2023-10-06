blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
blood_answer = {}

for blood_char in blood_type:
    if blood_char in blood_answer.keys():
        blood_answer[blood_char] += 1
    else:
        blood_answer[blood_char] = 1

print(blood_answer)