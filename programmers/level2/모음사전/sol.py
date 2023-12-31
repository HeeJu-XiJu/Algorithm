# from itertools import permutations
# def solution(word):
#     words = ['A', 'E', 'I', 'O', 'U']
    
#     searchlist = set(words)
#     searchwords = words * 5
#     for num in range(2, 6):
#         permutation = permutations(searchwords, num)
#         permutation = set((permutation))
#         for str in permutation:
#             searchlist.add(''.join(str))
#     answer = sorted(searchlist).index(word) + 1
    
#     return answer

# print(solution('AAAAE'))


# 이진탐색

from itertools import permutations
def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    
    searchlist = set(words)
    searchwords = words * 5
    for num in range(2, 6):
        permutation = permutations(searchwords, num)
        permutation = set((permutation))
        for str in permutation:
            searchlist.add(''.join(str))

    searchlist = sorted(searchlist)
    left = 0
    right = len(searchlist)
    while left <= right:
        middle = (left + right) // 2
        if word == searchlist[middle]:
            return middle + 1
        elif word < searchlist[middle]:
            right = middle - 1
        else :
            left = middle + 1

print(solution('AAAAE'))