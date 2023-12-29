from itertools import permutations
def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    
    searchlist = set(words)
    searchwords = words * 5
    for num in range(2, 6):
        permutation = permutations(searchwords, num)
        searchlist.add(list(permutation))
    print(searchlist)
    # print(sorted(['A', 'AA', 'AE', 'EA', 'E']))
    answer = 0
    
    return answer

print(solution('AAAAE'))