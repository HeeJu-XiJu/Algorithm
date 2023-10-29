def solution(k, score):
    answer = []
    stack = []
    for i in score:
        if len(stack) < k:
            stack.append(i)
            answer.append(min(stack))
        else:
            if min(stack) <= i:
                stack.remove(min(stack))
                stack.append(i)
                answer.append(min(stack))
            else:
                answer.append(min(stack))
    return answer

print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))

# 다른 풀이
# 굳이 min(stack)과 i를 비교할 필요없이 i값을 추가한 후 가장 작은값을 제거하여 answer에 넣으면 됨
stack.append(i)
if len(stack) > k:
    stack.remove(min(stack))
answer.append(min(stack))

    