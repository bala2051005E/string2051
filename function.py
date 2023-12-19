#def greeting():
#    print("hi there")

#print("start")

#greeting()

#+print("end")

#ef loop(a):
#    for i in range(1, a - 1):
#        print(i)

#loop(10)

#print("end")

#l1 = []
#l2 = []

#def createlist(n):
#   for i in range(1, n + 1):
#      l1.append(i)
        

#createlist(15)
#print(l1)
#l1.clear()
#print("end")

#createlist(5)
#print(l1)

#print("end")


#def loop (n):
#    for i in range(1, n + 1):
#        print(i)

#loop(20)
#print("end")
#loop(5)
#print("end")        


# 1) 

 
#values = [9,7,10,6,8] 
  
#print(sorted(values))

#def calculation(a, b):
#    return a + b, a - b, a * b, a / b

#add, sub, multi, div = calculation(20, 60)
#print(add, sub, multi, div)

#2)

#def func1(*args):
#    for i in args:
#        print(i)

#func1(20, 40, 60)
#func1(80, 100)


#l1 = [1,3,5,7,9]
#l2 = [2,4,6,8,10]
#l3 = [11,21,31,41,51]


#def reverse_values(*args):
#    reversed_values = []

#    for value in args:
#        if isinstance(value, str):
#            reversed_values.append(value[::-1])
#        elif isinstance(value, list):
#            reversed_values.append(value[::-1])  
#        else:
           
#            reversed_values.append(value)

#    return tuple(reversed_values)

#original_values = "Hello", [1, 2, 3], "redrum"
#reversed_result = reverse_values(*original_values)

#print(reversed_result)


#def variables (n):
#    for i in range(1, n + 1):
#        print(i)

#variables(5)
#print(l1)
#l1.clear()
#print("end")

#variables(15)
#print(l2)
#l2.clear()
#print("end")


#variables(60)
#print(l3)
#l3.clear()
#print("end")


original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print(original_list)


def custom_reverse(seq):
    reversed_seq = []
    for i in range(len(seq) - 1, -1, -1):
        reversed_seq.append(seq[i])
    return reversed_seq

# Usage
original_list = [1, 2, 3, 4, 5]
reversed_list = custom_reverse(original_list)

print(reversed_list)















