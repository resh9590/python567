

old_list =[4, 5, 5, 6, 7, [], 3, [],9]
print ("old list", old_list)

new_list =([x for x in old_list if x ])

print ("new list", new_list)