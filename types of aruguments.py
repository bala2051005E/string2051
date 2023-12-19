# arbitary arguments

def student(firstname, lastname ='Mark', standard ='Fifth'):

	print(firstname, lastname, 'studies in', standard, 'Standard')

def greet(name):
    print("Hello, " + name + "!")

# Call the function with an argument
greet("Alice")

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Call the function with positional arguments
greet("Alice", 30)

# keyword aruguments

def nameAge(name, age):
	print("Hi, I am", name)
	print("My age is ", age)

print("Case-1:")
nameAge("Rafeel", 27)

print("\nCase-2:")
nameAge(20, "Raiden")


