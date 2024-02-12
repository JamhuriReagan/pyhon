# DataType

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
is_python_interesting = True  # bool

# a variables with multiple values
languages = ["python ", "php", "java", "kotlin"]  # list
fruits = ("apple", "banana", "orange", "pear",)  # Tuple
countries = {"Kenya", "Ghana", "China"}  # set

# Dictionary
details = {
    "firstname": "Reagan",
    "course": "MIT",
    "Age": 19,
    "Nationality": "Kenya"
}

print(number)
print(num)
print(greeting)
print(is_python_interesting)
print(countries)
print(details)
print(details["firstname"])
print(details["Nationality"])

# Determining the data typeof a variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting  one datatype to another
print(float(number))
print(int(num))
