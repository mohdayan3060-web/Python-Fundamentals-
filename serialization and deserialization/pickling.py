# pickling is process where python object convert into binary bytes 
#unpickling is reverse operation in which binary file converted  into object
import pickle #always improt pickle when you want to use it 
class person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def display_info(self):
        print(f"my name is {self.name} and my gender is :{self.gender} and i {self.age} years old ") 

obj=person('ayan','male',20)

with open('person.pkl','wb') as f:
    pickle.dump(obj,f)
   

with open('person.pkl','rb') as f:
    obj=pickle.load(f)  

print(obj.display_info())

#pickle vs JSON

     
    

