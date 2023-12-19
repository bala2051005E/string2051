#a = "who am i"
#print(a[::-1])

s = input("Enter a string: ")
str = ""
for i in s:
    str = i + str
print("The reversed string is : ", end="")
print(reversed(s))  




def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Geeksforgeeks"


print("The reversed string is : ", end="")
print(reverse(s))