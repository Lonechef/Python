def square(x):
    return x**2
print(square(5))

# def sum(x,y):
#     return x+y
# print(sum(4,5))

def multi(x,y):
    return x*y
print(multi("Saumya",3))

import math
#Here we can also written two values
def circle_stats(radius):
    area = math.pi * radius **2
    circumference = 2*math.pi*radius
    return area,circumference
print(circle_stats(5))

# Lambda FUnctions
cube = lambda x: x**3

print(cube(4))


#Arguments SO for Passig multiple arguments you just need to do *args
def  sum_all(*args):
    #In Python we have the in built method which is called as sum
    for i in args:
        print(i*3) 
    return sum(args)

print(sum_all(1,2,2,3))
# Baasically in backend the basically the args is accepted as tuple so if you want you can  iterate over that also


#To accept multiple kew and value pairs
def hello(**kwargs):
    for key, value in kwargs.items(): #Looping over all the items of it
        # For printing we are using the concrpt of the formatting Strig
        print(f"{key} {value}")

hello(name="Saumya",surname ="Parikh")

#Generator function with Yield
def even_generator(limit):
    for i in range (2,limit+1,2):
        return i
    
print(even_generator(10))  #So now  In this Basically over here issue is once loop run and this returns one number only

#Hence Bascially over here we will use yield instead of directly returning the value i

def new_even_generator(limit):
    for i in range (2,limit+1,2):
        yield i #Basically it will store the number

for num in new_even_generator(10): #So this Will accept a number everytime even gertatot is called
    print(num)