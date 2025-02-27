# Factory Functions in Python similar to JavaScript in this also we have this closure 
def chaicoder(num):
    def actualwork(x):
        return x**num #So this is returned when just actualWork is being called
    return actualwork #So this will be returned if in case chaicoder ibasically whole actual work

f = chaicoder(4)
g = chaicoder(3) 
print(f) #<function chaicoder.<locals>.actualwork at 0x7210a508f4c0 
print(g) #<function chaicoder.<locals>.actualwork at 0x7ac0c1393560>

print(f(4)) #So if we try to execulte the fucntion then we will get the value instead of gettign the refernece ans:256