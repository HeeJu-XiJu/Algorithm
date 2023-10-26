def solution(nums):
    N_2 = len(nums) // 2
    stack = []
    for i in nums:
        if i not in stack:
            stack.append(i)

    answer = min(N_2, len(stack))
    return answer

print(solution([3,3,3,2,2,2]))