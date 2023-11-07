# def solution(today, terms, privacies):
#     # 당일 년월일
#     today_y, today_m, today_d = today.split('.')

#     # 보증기간 dictionary
#     policy = {}
#     for i in terms:
#         mtype, month = i.split()
#         policy[mtype] = int(month)
    
#     answer = []
#     for i in privacies:
#         # date 가입기간 mtype 약관
#         date, mtype = i.split()
#         # 가입기간 년월일 분류
#         y, m, d = date.split('.')
#         # 가입 년 수 + 약관 년 수
#         y = int(y) + policy[mtype] // 12
#         # 가입 달 수 + 약관 달 수
#         m = int(m) + policy[mtype] % 12
#         if m > 12:
#             m = m % 12
#             y += 1
#         # 가입 일 수 - 1일
#         d = int(d) -1
#         # 가입일이 1일이면 전달28일로 변환
#         if d == 0:
#             m -= 1
#             d = 28

#         # 약정기간, 오늘 비교
#         if int(today_y) > y:
#             answer.append(privacies.index(i)+1)
#         else:
#             if int(today_m) > m:
#                 answer.append(privacies.index(i)+1)
#             else:
#                 if int(today_d) > d:
#                     answer.append(privacies.index(i)+1)
    
#         print(y, m, d)
#         print(int(today_y), int(today_m), int(today_d))
#     return answer

from datetime import datetime

def solution(today, terms, privacies):
    # 당일 년월일
    today_y, today_m, today_d = today.split('.')

    # 보증기간 dictionary
    policy = {}
    for i in terms:
        mtype, month = i.split()
        policy[mtype] = int(month)
    
    answer = []
    num = 1
    for i in privacies:
        # date 가입기간 mtype 약관
        date, mtype = i.split()
        # 가입기간 년월일 분류
        y, m, d = date.split('.')
        # 가입 년 수 + 약관 년 수
        y = int(y) + (policy[mtype] // 12)
        # 가입 달 수 + 약관 달 수
        m = int(m) + (policy[mtype] % 12)
        # m이 12월을 넘기면
        if m > 12:
            m = m % 12
            y += 1
        # 가입 일 수 - 1일
        d = int(d) -1
        # 가입일이 1일이면 전달28일로 변환
        if d == 0:
            d = 28
            m -= 1
        # 28일로 변환하면서 m이 0이 될 경우
        if m == 0:
            y -= 1
            m = 12

        # 약정기간, 오늘 비교
        if datetime(int(today_y), int(today_m), int(today_d)) > datetime(y, m, d):
            answer.append(num) privacies.index(i)
        num += 1
        
    return answer


print(solution("2020.05.15", ["A 1"], ["2001.01.10 A", "2001.01.10 A"]))
