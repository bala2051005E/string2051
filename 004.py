# map

# def multiply(n):

#  return n*n 

# num = (10,15,78,25) 

# result = map(multiply, num)

# print(list(result))

# # Filter

# numbers = [55, 92, 27, 48, 34, 62, 71, 18, 28, 43] 

# def numCheck(n):
#   if n < 50:
#     return False
#   else:
#     return True

# result = filter(numCheck, numbers)

# for n in result:
#   print(n)

# Reduce
  
# from functools import reduce

# def addition(a,b):    
#      return a+b

# n=map(int, input("Enter the numbers you want to add: ").split())

# reduce(addition,n)  


# ARGUMENTS

def fun(*arg):
	for arg in arg:
		print(arg)


fun('hello', 'Welcome', 'to', 'python programmmer')
