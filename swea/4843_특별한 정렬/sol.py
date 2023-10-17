import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    T2 = int(input())
    numbers = map(int, input().split())
    sort_numbers = sorted(numbers)
    answer = ''
    answer_list = [0] * 10
    for i in range(5):
        answer_list[2*i] = sort_numbers[-i-1]
        answer_list[2*i + 1] = sort_numbers[i]

    answer = ' '.join(str(char) for char in answer_list)

    print(f'#{tc} {answer}')