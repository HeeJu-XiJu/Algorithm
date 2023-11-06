# def solution(s, skip, index):
#     answer = ''
#     for i in s:
#         count = 0
#         for j in skip:
#             if ord(j) in range(ord(i), ord(i)+index+1) or ord(j) in range(97, ord(i)+index-25):
#                 count += 1

#         if ord(i)+count+index > 122:
#             answer += chr(ord(i)+count+index-26)
#         else:
#             answer += chr(ord(i)+count+index)
        
#     return answer

def solution(s, skip, index):
    answer = ''
    mlist = []

    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in skip:
            mlist.append(chr(i))

    for i in s:
        answer += mlist[(mlist.index(i)+index) % len(mlist)]

    return answer
print(solution("aukks", 'wbqd', 5))