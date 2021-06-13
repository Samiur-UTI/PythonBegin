#Codeforces problem
charm = input('Enter a nice array')
arr = [char for char in charm.split()]
print(list(map(lambda x: int(x, 10) , arr)))
## Create an object from a tuple
tup = [('lulu',25),('Prince',0),('Rafi',50)]
pimp = {key:value for key,value in tup}
print(pimp)