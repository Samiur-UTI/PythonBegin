#Print all unique pairs in an array 
arr = [1,2,3,4,5,6]
def pairs(li):
  for i in li: 
    for j in li:
        if i != j:
            print(f"{i},{j}")
pairs(arr)
