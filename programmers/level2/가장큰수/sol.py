# def solution(numbers):
#     answer = ''
#     temp = ''
#     while len(numbers) > 0:
#         for number in numbers:
#             if temp == '':
#                 temp = str(number)
            
#             number1 = temp + temp[0] * (4-len(temp))
#             number2 = str(number) + str(number)[0] * (4-len(str(number)))

#             if number1 < number2 :
#                 temp = str(number)
#             elif number1 == number2 and len(temp) > len(str(number)):
#                 temp = str(number)
#         answer += temp
#         numbers.remove(int(temp))
#         temp = ''

#     return answer


# def solution(numbers):
#     answer = ''
#     temp = ''
#     while len(numbers) > 0:
#         for number in numbers:
#             if temp == '':
#                 temp = str(number)
#             else:
#                 number1 = temp * 3
#                 number2 = str(number) * 3
#                 if int(number1[:3]) < int(number2[:3]):
#                     temp = str(number)
#                 elif int(number1[:3]) == int(number2[:3]) and len(temp) > len(str(number)):
#                     temp = str(number)
#         answer += temp
#         numbers.remove(int(temp))
#         temp = ''

#     return answer



# 다른 풀이
def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))
print(solution([3, 30, 34, 5, 9]))


# 다른 풀이2
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer