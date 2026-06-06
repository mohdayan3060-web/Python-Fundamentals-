#namespace decorators and iterators 

#Namespace =>namespace  are dictionary of identifiers(keys ) and their object(values )
#type of name space => 1. built in ,globl,enclosed  and local name space 

#LEGB Rule ()

#local and global scope 
# using local scope you can access global variable  you can view it but can not be update and modify it (you can make chnage using global)

a=10
def pr():
    # global a
    # a+=12
    print(a)

pr()
print(a)


#built-in scope =>print/type/min/sorted/input/true /false   is example of built-in 
import builtins # to see how many built-in function 
print(dir(builtins))


#Enclosing scope 

def outer():
    num=10
    def inner():
        nonlocal num #nonlocal is used to change the var in enclosing scope through inner (local scope )
        num +=10
        print("innerscope /localscope ")
    inner()
    print("this non_local or enclosing scope ")

outer()
print("this is global scope , main program")


#local then enclosing then global then built-in 

