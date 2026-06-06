#Decorators =>Decorators is function that recive function and as input and adds some functionality then return it 
#python function are first class citizen ?

#two type of decorators ,1.built-in decorators => @property, @staticmethods
# 2. user define decoraors 

# closuer fuction means the inner function can accesss the variable /function of outer funtion after they return 

def my_decorators(func):
    def wrapper():
        print("*******************************")
        func()
        print("*******************************")

    return wrapper

def hello():
    print("hello")

a=my_decorators(hello)
a()    


#shortcut (important methods )

def my_decorators(func):
    def wrapper():
        print("*******************************")
        func()
        print("*******************************")

    return wrapper
@my_decorators
def hello():
    print("hello")


hello()

#decorators to find the execution time of any function 
#meaningfull example 

import time

def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print('time taken by ',func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def greeting():
    print("goodmorning everyone ")
    time.sleep(2)

a=10
b=20
@timer
def sum(a,b):
    time.sleep(2)
    print(a+b)    

greeting() 
sum(a,b)   
    
#another example is    : Sanity check(checking the data type )

#dataclass in python

