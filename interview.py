Codeforces problem
charm = input('Enter a nice array')
arr = [char for char in charm.split()]
print(list(map(lambda x: int(x, 10) , arr)))
## Create an object from a tuple
tup = [('lulu',25),('Prince',0),('Rafi',50)]
pimp = {key:value for key,value in tup}
print(pimp)
#Google interview question
array = [2,5,1,2,3,5,1,2]
array2 = [3,5,4,9,3,7,5]
def reccurance(array):
    for items in array:
        for i in array:
            if i == items:
                return i
def reccurance2 (arr):
    x = {}
    for i in arr:
        if i in x:
            return i
        x[i] = 1
    return 'nothing found'
    


print(reccurance2([3,2,2,4]))        
            