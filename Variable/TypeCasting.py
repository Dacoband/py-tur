# typecasting = The process of converting a value of one data type to (string , int, float, boolean)
#                                                                        Expicit vs Implicit

name = "volka"
age = 21
gpa = 3.1
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#################################################################

age = float(age)
print(age)
print(type(age))

#################################################################

# Implicit

x = 2
y= 2.0

x = x/y
print(x)