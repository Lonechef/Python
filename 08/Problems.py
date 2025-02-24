#Que 1
userage = input("Please provide me a age: ")
intage = int(userage)
if intage<13:
    print("Child")
elif intage<20:
    print("Teenager")
elif intage<59:
    print("Adult")
else:
    print("Senior")

#Que 2
age = int(input("Please Enter the age : "))
day = input("Please Enter the Day : ")
if(day=="Wednesday"):
    if(age>=18):
        print(10)
    else:
        print(6)
else:
    if(age>=18):
        print(12)
    else:
        print(8)
