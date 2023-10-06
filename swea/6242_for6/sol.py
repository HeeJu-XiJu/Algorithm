blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict1 = {
    'A': 0,
    'O': 0,
    'B': 0,
    'AB': 0,
}

for blood1 in blood_list:
    blood_dict1[blood1] += 1

print(blood_dict1)

#################

blood_dict2 = {}

for blood2 in blood_list:

    if blood2 in blood_dict2.keys():
        blood_dict2[blood2] += 1
    else:
        blood_dict2[blood2] = 1
    
print(blood_dict2)