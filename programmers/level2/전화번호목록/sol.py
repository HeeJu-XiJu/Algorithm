def solution(phone_book):
    hash = {}
    for i in phone_book:
        hash[i] = 1
    
    for i in phone_book:
        mstr = ''
        for j in i:
            mstr += j
            if mstr in hash.keys() and mstr != i:
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))