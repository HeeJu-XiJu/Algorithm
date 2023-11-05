def solution(nums):
    answer = 0
    mlist = []

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                mlist.append(nums[i]+nums[j]+nums[k])
    
    for i in mlist:
        num = 0
        for j in range(2, i):
            if i % j == 0:
                num += 1
        if num == 0:
            answer += 1
    return answer

print(solution([1,2,7,6,4]))