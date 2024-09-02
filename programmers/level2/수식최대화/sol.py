from itertools import permutations
from collections import deque

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    else:
        return str(int(num1) * int(num2))

def solution(expression):
    mlist = deque()
    num = ''
    for e in expression:
        if e.isdigit():
            num += e
        else:
            mlist.append(num)
            mlist.append(e)
            num = ''
    mlist.append(num)
    
    priority = list(permutations(['+', '-', '*'], 3))
    result = 0
    for p in priority:
        mlist2 = mlist.copy()
        for op in p:
            stack = deque()
            while len(mlist2) != 0:
                temp = mlist2.popleft()
                if temp == op:
                    stack.append(operation(stack.pop(), mlist2.popleft(), op))
                else:
                    stack.append(temp)
            mlist2 = stack
        result = max(result, abs(int(mlist2[0])))
    return result

print(solution("100-200*300-500+20"))