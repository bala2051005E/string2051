# Python program to reverse a string using for loop

# take inputs
string = 'Know Program'

# find reverse of string
reverse = ''
for i in range(len(string), 0, -1):
   reverse += string[i-1]

# print reverse of string
print('The reverse string is', reverse)