original_dict = [{'name': 'dfg', 'age' : 20}, {'name' : 'abc', 'age': 15},{'name' : 'hjk', 'age' : 45}]

print(sorted(original_dict, key= lambda i : (i['age'], i['name'])))
