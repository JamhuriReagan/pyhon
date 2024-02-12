temperature = 32

if temperature > 37:
    print('It is hot')
else:
    print('it is cold')

# A program that print the largest number among three numbers
num1 = 45
num2 = 89
num3 = 32
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that print the largest number among three numbers
if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")

# A program that checks whether a number is even or odd
number = 56
if number % 2 == 0 :
    print(number,"is even")
else :
    print(number,"is odd")


# a program that checks whether a number is  prime or not

number = 12
if number == 1:
    print(number, "is not a prime number")
elif number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
            print (i , "times" , number // i , "is" , number)
            break
    else:
        print(number, "is a prime number")

