import numpy as np

#np.sort (give numpy array sorted )
# numpy.sort(a, axis=-1, kind=None, order=None, *, stable=None)  axis=0(column wise sorting (verticaly)) axis=1(row wise sorting(horizentaly))
print("Numpy hidden Function \n")
# random.randint(low, high=None, size=None, dtype=int)
a=np.random.randint(1,1000,50)
b=np.random.randint(10,300,24).reshape(4,6)
# print(np.sort(a))
# print(np.sort(b))
#for decreasing order 
# print(np.sort(a)[::-1])


#np.append()  append element at last
#append in 1D
print(np.append(a,200))
#append in 2d
print(np.append(b,np.zeros((b.shape[0],1)),axis=1))

#np.concatinate 
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)

print(np.concatenate((c,d),axis=1))

#np.unique
e=np.array([1,2,32,32,111,1,1,1,34,56,44,44,333,32211,1,111,221,221])
print(np.unique(e))

#np.expand_dims  (Expand dimentions )
print(np.shape(b))
print(np.expand_dims(b,axis=0).shape)

#np.where (give indeces of input array  where the condtion is satisfied )
print("index position is : ",np.where(a%2==0))
#np.where(Conditions,true,false)
print("index postion is : ",np.where(a>20,1,0))

#np.argmax (return indices of the max elements of an array in particular axis )
#np.argmin
print(a)
print("Index positions is : ",np.argmax(a))
print("Index positions is : ",np.argmin(a))

# np.cumsum (cummulative sum )
print(np.cumsum(a))

#np.cumprod (cummulative products)
print(np.cumprod(a).round())

#np.percentile
# compute the nth percentile of given data (array elemnts ) along the specific axis 
print(np.percentile(a,50))
print(np.median(a))

#histogram 
# computes the numerical frequency distribution of a dataset by splitting it into distinct intervals (bins) and counting how many values fall into each interval
print(np.histogram(a,bins=[0,100,200,300,400,500,600,700,800,900]))

#np.corrcoef ( calculates the Pearson product-moment correlation coefficient matrix for given input data)
salary=np.array([20000,40000,25000,35000,60000])
expr=np.array([1,3,2,4,2])
print(np.corrcoef(salary,expr))

#np.isin (use this to check the multiple item present in  array or not i tgives in true and false )
print(a)
item=[100,232,432,456,764,800,90,867,236,786]
print(a[np.isin(a,item)])

#np.flip()  create mirror imaage 
print(np.flip(item))

#np.put  (put element at specific array )
# np.put(arrayname,[index01,index02],[elementAtIndex01,elementAtIndex02])
    