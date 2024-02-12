# while loop
# Incrementing a value
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrementing value
num1 = 105
while num1 >= 100:
    print(num1)
    num1 -= 1

# Break statement
X = 1
while X <= 5:
    print(X)
    if X == 3:
        break
    X += 1

# continue statement
count = 19
while count < 25:
    count += 1
    if count == 23:
        continue
    print(count)

# For loop
languages = ["python", "c++", "kotlin"]
for lang in languages:
    print(lang)

# Range
for z in range(6):
    print(z)

for y in range(20, 31):
    print(y)

for i in range(30, 41, 2):
    print(i)

for letters in "innovation":
    print(letters)
