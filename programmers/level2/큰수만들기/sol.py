# 문제를 잘못 이해했다...
# def solution(number, k):
#     numbers = list(map(str, number))
#     numbers.sort(reverse=True)
#     for _ in range(k):
#         numbers.pop()
#     answer = ''.join(numbers)
#     return str(answer)

# 런타임에러
# def solution(number, k):
#     remove = 0
#     numbers = list(map(int, number))
#     answer = ''

#     while remove != k:
#         maxnumber = 0
#         for idx in range(len(numbers)):
#             if idx > k - remove:
#                 break
#             if maxnumber < numbers[idx]:
#                 maxnumber = numbers[idx]
        
#         maxidx = numbers.index(maxnumber)
#         remove += maxidx
#         answer += str(maxnumber)

#         for _ in range(maxidx+1):
#             numbers.remove(numbers[0])
        
#     for num in numbers:
#         answer += str(num)

#     return answer


def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

# print(solution("1924", 2))
print(solution("1231234", 3))