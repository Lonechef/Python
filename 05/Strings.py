numString = "012345678"
print(numString[0:7:2]) #This is another way to slice basiically in this we can do gap of 2 so indexing gap 2 can be considered (2-0) , (4-2) so it will be 0246
chai ="Masala Chai"
 # To convert  to lower case
print(chai.lower())
print(chai.upper())
newchai = "   Masaala Chai  "
print(newchai.strip()) # This is helpful to remove all the extrea spaces 
#As string is immutable the originally assigned chai will remain same only
chai.replace("Masala Chai","Ginger Tea")
print(chai)

# Converting String to List
chai ="Lemon, Ginger, Masala"
#So  in this basically you can do BY the split
print(chai.split(", ")) #SO in this we jsut have to mention on what basis I want to split
#To find any character in a particular stringc
chai = "Masala Chai"
print(chai.find("Chai")) #So this tells from whihc index that particular string is present
# And in case no string like that is found then it will give me -1 which basically means there is nothing like that
#To count how many time a particular substring is present in the String
chai = "Masala Chai Chai Chai Chai"
print(chai.count("Chai"))
# In this we have a order formatting in Python
chai_type ="Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity,chai_type)) #So By doing order format we can write up a string
# Converting List to the String
chai_variety =["Lemon","Masala","Ginger"]
print("".join(chai_variety)) #So in this Basically this will directly join all elements to list and convert it to one String Output ; LemonMasalaGinger
print(" ".join(chai_variety)) #Join and leave the Space in between Lemon Masala Ginger
chai = "He said, \"Masala Chai is best\" " #This is helful when we have multiple double quotes in our system  
print(chai)
chai = "masala\nchai"
print(chai_type) #So in this it will consider the masala and chai in the new line
# But incase if we want that chia and \n in one line only inthat case basically we will use
chai = r"masala\nchai"
print(chai) #So basically in this r is considered as the raw string and directly it will be considered 