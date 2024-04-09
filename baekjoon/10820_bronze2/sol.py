import sys
sys.stdin = open('input.txt')

while True:
    try:
        mlist = [0] * 4
        com = input()
        for s in com:
            if 'a' <= s <= 'z':
                mlist[0] += 1
            elif 'A' <= s <= 'Z':
                mlist[1] += 1
            elif '0' <= s <= '9':
                mlist[2] += 1
            elif ' ' == s :
                mlist[3] += 1
        print(*mlist)
    except:
        break