# out of range + 2번째 케이스 2가 나옴.. 반올림을 해도 왜지?
# def solution(people, limit):
#     people.sort()
#     answer = 0
#     while len(people) > 1:
#         p = people.pop()
#         if p + people[0] > limit:
#             answer += 1
#         else:
#             people.append(p)
#             break
#     answer += round(len(people) / 2)

#     return answer

# 오답 처리
# from math import ceil
# def solution(people, limit):
#     people.sort()
#     answer = 0
#     while len(people) > 1:
#         p = people.pop()
#         if p + people[0] > limit:
#             answer += 1
#         else:
#             people.append(p)
#             break
#     answer += ceil(len(people) / 2)

#     return answer


from collections import deque
def solution(people, limit):
    people.sort()
    mypeople = deque(people)

    answer = 0
    while len(mypeople) > 1:
        l = mypeople.pop()
        s = mypeople.popleft()
        if l + s > limit:
            mypeople.appendleft(s)
            answer += 1
        else:
            answer += 1
    if len(mypeople) == 1:
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))


# 정리된 풀이
from collections import deque
def solution(people, limit):
    boat = 0
    people = deque(sorted(people))

    while people:
        saved = people.pop()
        boat += 1

        if (people) and (saved + people[0] <= limit):
            people.popleft()

    return boat