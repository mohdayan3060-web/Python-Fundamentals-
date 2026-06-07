import numpy as np
import time

#learn about  module and packgeses 
#numpy array vs python list 
#Based on speed (list is dynamic in size  and it  also refrencial array )
# a=[ i  for i in range(10000000)]
# b=[ i for i in range(10000000,20000000)] 
# c=[]
# start =time.time()
# for i in range(len(a)):
#     c.append(a[i]+b[i])

# print(time.time()-start)

#using numpy array(fixed size array and  store item in contigious memory location becouse behind the sceen numpy array used  c programing language arraya )

# x=np.arange(10000000)
# y=np.arange(10000000,20000000)

# start=time.time()  #tell  current time 
# c=x+y
# print(time.time()-start)


#based on memory 
# a=[i for i in range(10000000)]
# import sys 

# print(sys.getsizeof(a)) #get the size of data 


# b= np.arange(10000000 ,dtype=np.int16)
# print(sys.getsizeof(b))

#why the numpy array is better then python list 
# fast speed , convince , and comsume less memeory becz you have flexbilty 
# ----------------------------------------------------------------------------------------------------------------  
#Adavnce indexing 
a1= np.arange(24).reshape(6,4)
print(a1[0:4:3,0:3])
#fancy indexing (you pass list )
print(a1[[0,2,3,5]])
print("\n")
#boolean indexing 
a2=np.random.randint(1,100,24).reshape(6,4)
print(a2)
#find the number greater then 30
print(a2[a2>30]) #booloean wraping 

#find even number 
print(a2[a2%2 !=0])
#both condition combined 

print(a2 [(a2>50)&(a2%2 ==0) ]) #here we we bitwise &  becz we are dealing with boolean 

#dvisible by 7
print(a2[a2%7==0])

#Broadcasting  [NumPy alag-alag shapes (dimensions) ke arrays par bhi mathematical operations (jaise addition, subtraction, multiplication) karne deta hai, bina bade array ki copy banaye]
# smaller array get strech for compitible with larger shape arraya 

#braodcasting rule ==> 
# Dono dimensions barabar (equal) honi chahiye.
# Ya fir unme se koi ek dimension 1 honi chahiye.

# a3=np.arange(12).reshape(3,4)  #back se comapare karo ya to same hone chahiye ya toho 1 hona chahiye 
# a4=np.arange(12).reshape(4,3)
# print(a3+a4)


a3=np.arange(3).reshape(3,1)  #back se comapare karo ya to same hone chahiye ya toho 1 hona chahiye 
a4=np.arange(3).reshape(1,3)
print(a3+a4)


#working with maths formulas 

a6=np.arange(10)
print(a6)

#sigmoid (making their won)

def sigmoid(array):
    return  1/(1+np.exp(- array))

print(sigmoid(a6)) 

#mean squared error (loss function )
actual=np.random.randint(1,50,25)
prediction= np.random.randint(1,50,25)

def mse(actual,prediction):
    return  np.mean(actual-prediction)**2
#catagorical cross predictions 

print(mse(actual,prediction))

def cce(actual,prediction):
    return  -np.sum(actual*np.log(prediction))

print(cce(actual,prediction))

# how to deals with missing value 
# np.nan=>mising values 
a7=np.array([1,2,3,4,np.nan,6])
print(a7)

print(a7[~np.isnan(a7)]) #check the is you are misisng values  and alos use booleans indexing 

#polating graphs 
#x1=y1
x1=np.linspace(-10,10,100)
y1=x1

import matplotlib.pyplot as plt
plt.plot(x1,y1) 
# plt.show() #this is used for showing the graph 

#y=x^2
# x=np.linspace(-10,10,50)
# y=x**2

# plt.plot(x,y)
# plt.show()

# y=sin(x)

x=np.linspace(-10,10,200)
y=np.sin(x)
plt.plot(x,y)
plt.show()


# y=xlog(x)
y=np.log(x**x)
plt.plot(x,y)
plt.show()


#using numpy and matplotlib draw 3d graph 
# import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(projection='3d')


