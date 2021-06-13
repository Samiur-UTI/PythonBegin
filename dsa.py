# #Print all unique pairs in an array 
# arr = [1,2,3,4,5,6]
# def pairs(li):
#   for i in li: 
#     for j in li:
#         if i != j:
#             print(f"{i},{j}")
# pairs(arr)
# #Reverse a string
# string = 'Akak ihsihS';
# def reverser(str):
#   result = ''
#   for i in str[::-1]:
#     result += i 
#   return result
# print(reverser(string))
# #Merge sorted arrays
# dataA = [1,2,3,4,5,6,7,8,9]
# dataB = [21,34,53,56]
# def sorter(a, b):
#     new_list = a+b
#     return sorted(new_list)
# print(sorter(dataA, dataB))
##Hash Tables
table = {
    'name': 'Samiur',
    'age': 36,
    'gender': 'Male',
    'power' : lambda x:x*5 
}
print(table)
