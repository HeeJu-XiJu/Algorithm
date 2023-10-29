import datetime

def solution(a, b):
    week = ['FRI','SAT', 'SUN','MON','TUE','WED','THU']
    date = datetime.date(year = 2016, month = a, day = b)
    first = datetime.date(year = 2016, month = 1, day = 1)
    day = date - first
    answer = week[int(day.days) % 7]
    return answer

print(solution(5, 24))