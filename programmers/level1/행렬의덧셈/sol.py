def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer_list = []
        for j in range(len(arr1[0])):
            answer_list.append(arr1[i][j] + arr2[i][j])
        answer.append(answer_list)
    return answer

print(solution([[1],[2]], [[3],[4]]))

# 다른 풀이
# 0으로 채워진 행렬을 만든 후 채우는 방식
def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = (arr1[i][j] + arr2[i][j])
    return answer

# 다른 풀이
# zip 사용
def solution(arr1, arr2)::
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(arr1,arr2)]
    return answer