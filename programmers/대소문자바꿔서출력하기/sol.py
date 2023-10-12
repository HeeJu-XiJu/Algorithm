str = input()
for char in str:
    if char.islower() == True:
        print(char.upper(),end = '')
    else :
        print(char.lower(),end = '')