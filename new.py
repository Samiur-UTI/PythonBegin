my_list = [(0,2),(4,3),(9,9),(10,-1)]
##print(sorted(list(map(lambda x:x*x,my_list)),key=None,reverse=True))
print(sorted(my_list,key=lambda x:x[1],reverse=False))
another_list = [char for char in 'samavuda']
another_list2 = [char for char in list(map(lambda x:x*2,range(0,100)))]
my_dict = {key:value**2 for key,value in {'a':2, 'b':4}.items()}

original = ['a','b','c','d','e','b','d','a']

duplicate = [char for char in original if original.count(char) > 1]


print(another_list)
print(another_list2)
print(my_dict)
print(list(set(duplicate)))