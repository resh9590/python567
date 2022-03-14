test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " ,test_list)

result = []
for i in test_list:
    if i  not in result: 
        result.append(i)

print ("finial list", result)