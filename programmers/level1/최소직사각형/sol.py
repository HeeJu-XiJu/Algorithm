def solution(sizes):
    w = 0
    h = 0
    for a, b in sizes:
        if a >= b :
            if w < a:
                w = a
            if h < b:
                h = b
        else:
            if w < b:
                w = b
            if h < a:
                h = a

    answer = w * h
    return answer

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

# 다른 풀이
w = [] 
h = [] 

for i in sizes:
    w.append(max(i))
    h.append(min(i))

answer = max(w) * max(h)