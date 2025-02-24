chai_types ={"ABC":123,"BCD":456,"GHI":7890}
for chai in chai_types:
    print(chai) #This will basically print all the keys 
    print(chai,chai_types[chai]) #THis will print both keys and the values 

# Another way to iterate over Dictionary is basically
for key, values in chai_types.items(): #So as it is dictionary so in this basically in this we have to consider  the items of the dictionary
    print(key,values)

#To find if any particular key is present in it or not
if "ABC" in chai_types:
    print("Yes abc in present in the Dictionary")

print(len(chai_types))

#TO add a new key
chai_types["HJI"]=4566
print(chai_types)
 
#To pop for dictionary we need to mention the which key we need to pop out 
chai_types.pop("HJI")
print(chai_types)

#Another way to pop is basically do popitem
chai_types.popitem() #So by default it will pop the last element of the dictionary
print(chai_types)

#TO delete a particular keu
del chai_types["ABC"]
print(chai_types)

# Kinda Nested Dictionary
tea_shop = {"chai":{"Masala":"spicy","Ginger":"Zesty"},
            "Tea":{"Lemon":"Sour","Green":"bitter"}
}
print(tea_shop)
print(tea_shop["chai"]["Masala"]) #SO now in this basically we will get the value in case for chai->Masala that is spicy

sqaured_nums ={x:x**2 for x in range(8)}
print(sqaured_nums)
# Empty
sqaured_nums.clear()
