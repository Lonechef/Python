# Internal Working of Python
# Lets Say we have a memory Block and in that Block we have 10 Basically Now that 10 will become object when any variable will refer to it 
# So lets say we have a variable score referring to 10 score->10
# Now lets say there is also another variable called as ascore that vaklue is also 10 so it will also refet to 1o so it will also point to the same 10 present
# in thhe memory block so score,ascore -> 10
# Now lets say there is another variable a which is referring to 5  a-> 5 now lets say if delete a so now in memory space there is no refernce for 5
# So further it will be sent to garbage collector BY Python compiler but the process is a bit different 
# In Pythion basically ref_count basically in Pythion for particular value how much refernce is there is counted so for 10 ref_count will be 2
import sys
sys.getrefcount(24601)
print(sys.getrefcount(24601)) #Now  in this ans will be 3 so like python compiler may be assinging the number 3 to some refernce in python inside
print(sys.getrefcount('a')) #Now if we do this then in that Case we are getting 4294967295  So basically there is no way to see the refernce like this 
# In Pythnon the Jitni bhi data ki type hai wo memory mai hi allocate hoti hai like 10 hai wo hi define krta hai ki int hai ay string jo variable usko refer
# Krta hai usse matter nahi krta for example here score->10 the data type is defined based on 10 and not variable that is score 
# Python compiler  SO basically in python it treats string and integer a bit different like lets say in memory we have 3 and no vareiabke is assifgned to it so
# I wont remove that all of sudden it will take time and then remove it  because it will wai tif anyother variable will try to assign thmself 3 or not so 
# Everytime assign and reasddign wont be there Hence the garbage collection for string and interger is a bit late
# a= 5 SO here refence of 5 is assigned to a
# a = a+2 So now here a = 7 Now 5 has no reference hence after some while the 5 will be remove by garbage collector
myListOne = [1,2,3] # myListOne -> [1,2,3]
myListTwo = myListOne #myListTwo,myListOne -> [1,2,3]
myListOne ='chai' # Now myListOne -> chai & myListTwo -> [1,2,3]
# So now further basically 
myListOne = [1,2,3] # myListOne , myListTwo -> [1,2,3]
# Now as we know that Lists are mutable
myListOne[0]=55 # myListOne = [55,2,4]
print(myListOne)  # Output will be [55,2,4]
print(myListTwo) #Output will be [1,2,3] as for every new refernce is created in this
l1 =[1,2,3]
l2 = l1
print(l2)
l1[0]=44
print(l2)  #Now here the output will be [44,2,3] for l2 also now this is because in 1st examole mylistone is first assigned to [1,2,3] and then furthet
# mylistone is assigned to chai and then further it is assigned to [1,2,3] and furthe chages so in thhis mysListTwo will remain same
# But in above case l1,l2->[1,2,3] and then l1 is changes diretcly so this will also change l2
p1 = [1,2,3]
p2 = p1
p2 = [1,2,3]
p1[0]=66
print(p1)
print (p2) #Now in this [1,2,3] so basicallt over here here as 
# So basically the LIst is mutable so in that case for a particular variable it always assigns new refernce because if one os chnaged then another doesnot chnage 
h1 =[1,2,3]
h2 = h1[:] # So basically this we are doing slicing so h2 =h1[0:2] hence it takes from 0 to 2 but is nothing is there so it will take whole List
# So basically in this case a new copy of the h2 is xreated referring to diff [1,2,3] hence any change in h1 wont affect h2
# Hence we do slicing and all we make a copy basically
# Checking for the refernce
m = [1,2,3]
n = m
print(m==n) #THis will be true basically this checks the value
print(m is n) #This will basically it will also check the referenace hence now in this case the refetrnce for m and n is same so it will also be same
#But in case if we do 
n = [1,2,3] #So now if we expicitly define a variable in that casee basically new refernce will be createf
print( n is m) #So now it will be false 
 