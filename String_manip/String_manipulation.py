a="  Python is a"
b = " language"
name = "allen"
age = 20

#Concatenation
def concatenate(a,b):
    return a + b

print(concatenate(a,b))

#Slicing
def sliceing(a):
    a=a[1:5]
    return a
print(sliceing(a))

def formmatting(name,age):
    formatted_string = "{} is a {} years old".format(name,age)
    return formatted_string

print(formmatting(name,age))

def manipulation(a):
    return a.upper(),a.lower(),a.strip(),a.replace("Python" , "Java")

print(manipulation(a))