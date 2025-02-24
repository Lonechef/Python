list =["ABC","DEG","GHI"]
#TO see if any particular string exiusit in the 
if "ABC" in list:
    print("FOund") 
# pop will help to remove the laste element from the list
list.pop()
print(list)
# Now to remove a element from the array
list.remove("DEG") #This will remove DEG
print(list)
#To instert a value at a place
list.insert(1,"green")
print(list)
#SO if we do newList = list then in this basically the same reference is added rather then new
#But in case if we add the copy of that or create a new refernce only then a new refernce is created
newlistcopy = list.copy() #So in this case new refence is created 
#  So in list we can define a list without giving inpout like below
squared_nums = [x**2 for x in range(10)] # So this will take number from 0 to 10 and give us the sqaured numbers
print(squared_nums)
