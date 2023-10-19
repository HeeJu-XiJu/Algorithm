import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    string = str(input())
    answer = 1
    for char in string: # sting 하니씩 검사 
        if char == '(' or char == '{': 
            stack.append(char) # 시작괄호가 있다면 스택에 추가
        elif char == ')' or char == '}':
            if not stack: # 시작괄호가 없다면 0 반환
                answer = 0
      # pop으로 마지막 리스트를 꺼내 쌍이 맞지 않으면 0 반환
            elif char == ')' and stack.pop() != '(':
                answer = 0
            elif char == '}' and stack.pop() !='{':
                answer = 0
  
  # (( 와 같이 시작괄호가 두개가 스택에 있는 경우도 있기 때문에
  # 만약 stack 안에 시작 괄호가 남아있다면 0 반환
    if stack:
        answer = 0

    print(f'#{tc} {answer}')