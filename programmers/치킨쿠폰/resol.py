# 재귀함수로 풀어보기..?
def solution(chicken):
    coupon = 0
    left = chicken
    if left <= 9:
        return coupon

    coupon += chicken // 10
    left = chicken % 10 + coupon
    coupon += solution(left)

    return coupon

print(solution(1081))