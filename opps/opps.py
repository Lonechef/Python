class Car:
    brand = None
    model =None

#Creating Object og the class
#Here my_car is the object
my_car = Car()
print(my_car.brand) 


#Now lets Say we need to pass the value so in thi case the use __init__ will come
class newCar:
    #In inti we can pass the attributes that we Basically Need 
    #__init__ :This is simply like the constructor
    def __init__(self,userBrand,userCar):
        #Now as in JavaScript we use  this  so basically that is the link between my class and the object similarly in python we have self

        #So now we will make the brand as private now in puython we can make any thing private by applying "__" So that canot be user by any object of that class
        #It can be used only inside the class and further basically we need to make a getter method and use that variale
        self.__brand = userBrand
        self.model = userCar

        #Now for encapsulation making the brand as Private and adding a get method to acess the Brand
    def get_brand(self):
        return self.__brand

    #Making a function so basically in this the main thing is mandatory addition of the self
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    #Creating a Polymorphism basically in this we need to create mehod
    def fuel_type(self):
        return "Petrol or Diesel"

    

#Whevever you want to acess stuff which is inside the class we need to use self
my_newCar = newCar("Honda","Amaze")
# print(my_newCar.brand)

ny_newnewCar = newCar("Tata","Harrier")
print(ny_newnewCar)
print(my_newCar.full_name())
print(ny_newnewCar.get_brand())


#Inheritance.........
#So now in this ElectricCar is inhering newCar
class ElectricCar(newCar):
    def __init__(self,userBrand,userCar,Battery_size):
        #Now further there is no need to implementing self.userCar = userCar Rather we will be using the super keyWord super is basically inhering from the ancestors
        super().__init__(userBrand,userCar)
        self.Battery_size=Battery_size
    
    #Definfinf the same method fuel_type for the electric car
    def fuel_type(self):
        return "Electric Car"

my_electricCar = ElectricCar("Tata","Nexon Ev" ,"2.4")
print(my_electricCar.Battery_size)
#SO basically polymorphism tells us that the both are using same mehtod but can take diff values
#I0n above case the polymorphism is quite eaasy sometimes we can do polymorphism By taking two diff values like the attributes passed inside it are diff
print(my_electricCar.fuel_type())
safari = newCar("Tata","Safari")
print(safari.fuel_type())
#Encapsulation


#Polymorphism is basucally same method name but they behave in different manner





