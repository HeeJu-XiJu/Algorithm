from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = []
    if target not in words:
        return 0
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count
        for w in words:
            diff = 0
            for idx in range(len(word)):
                if word[idx] != w[idx]:
                    diff += 1
            if diff == 1:
                visited.append(w)
                queue.append([w, count+1])

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))