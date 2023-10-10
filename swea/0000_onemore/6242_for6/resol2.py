my_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
my_dict = {}
answer = 0

for blood_type in my_list:
    if blood_type in my_dict.keys():
        my_dict[blood_type] += 1
    else:
        my_dict[blood_type] = 1
    
print(my_dict)