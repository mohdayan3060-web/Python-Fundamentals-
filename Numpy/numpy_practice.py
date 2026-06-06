import numpy as np #always import numpy first before use it 

#creating 1d arraya 

a=np.array([1,2,3])
print(a)

# #2D(matrix) and 3D arrray(tensor)
print("2D array \n ")
b=np.array([[1,2,3],[2,1,4]])
print(b)
print("\n3D array  ")
c=np.array([[[10,20],[30,40],[50,40]]])
print(c)

# #Dtype
# print(np.array([1,2,0],dtype=bool))
# print(np.array([1,2,0],dtype=complex))
# print(np.array([1,2,0],dtype=float))

# #arange
x=np.arange(1,11)
print(x)
print(type(x))

# #reshape 
print(x.reshape(5,2))

# #np.ones 
print(np.ones((3,3)))#you need to provide tupples 
print(np.zeros((3,3)) )
print(np.random.random((3,3)))

# #linearlyspace (linspace ) #give points b/t two numbers 

np.linspace(-10,10,10,dtype=int)

# #np.identity
print(np.identity(3))

# #numpy array attributes 
# print("numpy attributes \n")
# a1=np.arange(10 )
# a2=np.arange(12,dtype=float).reshape(3,4)
# a3=np.arange(8).reshape(2,2,2)

# print(a1)
# print(a2)
# print(a3)

# #ndim(to check the dimention)
# print(a3.ndim)

# #shape (tell no of rows and columns )
# print("shape :",a2.shape)

# #size (tell the no.size ,overall size)
# print(a2.size)

# #itemsize(tell the each item take how much memeory)
# print(a1.itemsize)

# #dtype (tell the data type )
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)

# #changing datatype (to save memory storage )
#astype 
# print(a3.astype(np.int32))


# #Array openrations 
x1=np.arange(12).reshape(3,4)

x2=np.arange(12,24).reshape(4,3)

# print(x1)
# print(x2)

# #Scaler operations 
# # @airthmatic operation (+ - ,* ,/)
# print(x1+10)
# print(x1-10)
# print(x1*10)
# print(x1/10)


# #relation operators (give Answer into True and False )
# print(x1>4)
# print(x2<=10)

# #vectors operations 
# print(x1**x2)

#array function

arr01=np.random.random((3,3))
# print(arr01)
arr01=np.round(arr01*100)
print(arr01)

#max/min /sort/pro
# print(np.max(arr01,axis=0))  # 0=> colum and 1= roows  (flexiblity)
# print(np.min(arr01))
# print(np.sort(arr01))
# print(np.prod(arr01))

#mean/median/std/var
print(np.mean(arr01))
print(np.median(arr01))
print(np.std(arr01))
print(np.var(arr01))

#trigonometry function 
print(np.sin(arr01))

#dot product
print(np.dot(x1,x2))

#log and exponents
print(np.log(arr01))
print(np.exp(arr01))

#round/floor/ceil  (floor  mtlab ground(down) , ceil matlab roof (upper ))(remove decimal parts give the whole numbers only )
rnd= np.random.random((3,3))*100
print(rnd)
print(np.round(rnd))
print(np.ceil(rnd))
print(np.floor(rnd))


#indexing and slicing(through indexing you can fetch only one element  and through slicing you fetch multiple elements form  your matrix)
a1=np.arange(10 )
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

#slicing tricks matrix[row_start:row_end(execluded):step_sizing , col_start:col_end(excluded):step_sizing]
print(a3[0,0,0]) #this is for indexing
# matrix[row_start:row_end(execluded):step_sizing , col_start:col_end(excluded):step_sizing]
print(a2)
print(a2[0:2,1:3])
print(a2[0:2,1:4:2])  #(here step sizing is alSO used )
print(a2[0:3:2,1:4:2])
print(a2[1:2:3,0:4:3])


print(a3) 
#slicing in 3d [page,rows,columns]
#$$matrix[start:end:step, start:end:step, start:end:step]$$
print(a3[0:1,1:2,0:3])
print(a3[1:2,0:3,1:2])
print(a3[1:2,1:3,1:3])
print(a3[0:3:2,0:1:2,0:3:2])


# Itearting

for i in a1:
  print(i)

for i in a2:
  print(i)

for i in a3:
  print(i)

#Iteration on each individuls 
#nditer

for i in np.nditer(a3):
  print(i)


#transpose  (rows coumns exchnage )
print(a2)
print(np.transpose(a2))
print(a2.T) #shortcut methods 
# ravel [multi-dimensional array) ko khol kar ek single 1D array (flat line) bana deta hai.]
print(a2.ravel())
print(a3.ravel())

#stacking  [Numpy mein stack ka simple matlab hota hai multiple arrays ko aapas mein jodna (join karna) ek naye axis (dimension) ke saath.]
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)

#horigental  stacks 
hor_res=np.hstack((a4,a5))
print(hor_res)
# vertical stacks 

ver_res=np.vstack((a4,a5))
print(ver_res)

# spliting

print(np.hsplit(a4,2))
print(np.vsplit(a5,3))