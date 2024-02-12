# inbuilt functions
Y = max(10, 50, 93, 64, 57, 48)
print(Y)

X = min(10, 50, 93, 64, 57, 48)
print(X)

Z = pow(2, 3)
print(Z)


# USER-DEFINE FUNCTIONS
def details():
    print("Reagan")


details()  # Calling a function

# parameters and argument
def student (Name,course, age) :
    print(Name,course,age)

student("Reagan","Mit","19")
student("Madola","IT","30")

def employees(name,ID, Salary,Position,Age) :
    print(name,ID,Salary,Position,Age)

employees("John Kamau","28463746","400000","manager","55")
employees("Jane NJoki","26459398","406000","Secritary","65")
employees("Kenani Kimani","96735496","30000","Treasure","30")
employees("Alex Kamau","38564749","50000","Chairperson","70")
employees("Esther NJeri","37658959","100000","CEO","75")
employees("Preciouse Nikita","26378393","70000","Admin","35")
