#two type error (compile time and execution time )

#Index Error =>index error is thrown  when trying to access item at invalid index


#ModuleIsNotFound
#keyError 
#type error 
#Value error
#Name Error 
#Attribute error 
#file not found error


#Exception == during the runtime (logical error )
# why ? user experince and security

#when ever you deal with external file  that is reskiy  point  you should use try except block

# try:
#     apne code ko dalo 
# except:
#     ager error aya to kay show karoge us msg ka code likho     

with open('shmaple.txt','w')as f:
    f.write('hello wrolds ')

try:
    with open('shmaple.txt','r')as f:
        print(f.read())

except:
    print("file is not found !") 


#Cathing specific type error 

try:
    pass


except FileNotFoundError: #handel specific type of error 
    print("file is not found ")
except   NameError:
    print("variabe is not found ")

except Exception as e: #genric error (always in last )
    print(e)

#else  and finaly

try:
    pass
    # for test put your code here 

except:
    pass
    #If you got error 
    #when somting is wrong  in try  block then moved on except to check  which type of error 
else:
    pass
    #no error
    #when try block work properly and their is no error then moved  else block 
finally:
    
    #this block always execute 
    pass
        
#raise error 

class bank:
    def __init__(self,balance):
        self.balance=balance

    def withdrwal(self,ammount) :
        if ammount<0:
            raise Exception("Ammount can not be Negative ")
        if self.balance<ammount:
            raise Exception("insufficent balance")
        
        self.balance=self.balance-ammount   


obj=bank(1000)
try:
    obj.withdrwal(100)
except Exception as e:
    print(e)
else:
    print(obj.balance)

#note exception is class and e  behave as object 

#creating  your own exception class( make your exception class must be child of Exeption class )
class my_exception(Exception):
    def __init__(self,msg):

        print(msg)
class bank:
    def __init__(self,balance):
        self.balance=balance

    def withdrwal(self,ammount) :
        if ammount<0:
            raise my_exception("Ammount can not be Negative ")
        if self.balance<ammount:
            raise my_exception("insufficent balance")
        
        self.balance=self.balance-ammount   


obj=bank(1000)
try:
    obj.withdrwal(100000)
except my_exception as e:
    pass
else:
    print(obj.balance)

#why we create own exception class ?
# Custom exception classes tb banani hai jab aap apne application ke based se  kuch functionality  performe karni hoti hai 
#basically gadbad hone pai kuch karna  hai 
