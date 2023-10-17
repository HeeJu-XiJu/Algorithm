numbers = ['a', 'b', 'c', 'd']

n = len(numbers)

for i in range(1<<n):
    # print(i)

    temp = []
    for j in range(n):
        print(i, bin(i), bin(1<<j)) # bin(1<<j) 해당 자리에 1이 있는지 확인하는 연산
        # 1001 and 1 -> 1이 출력되므로 True
        # 1001 and 10 -> 0이 출력되므로 False

        if i & (1<<j):
            temp.append(numbers[j])
        print(temp)

    