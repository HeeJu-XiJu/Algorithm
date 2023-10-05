T = range(1, 201)
answer = []

for number in T:
    if number % 7 == 0 and number % 5 != 0:
        answer.append(str(number))

print(','.join(answer))