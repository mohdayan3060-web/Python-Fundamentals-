#working with binary file 
#how to  copy the image 


with open('img.png','rb') as f:
    with open('img_copy.png','wb') as wf:
        wf.write(f.read())


#working with big binary file 
#serialization uisng json module 
#list 
import json
l=[10,20,30,40,50,60,70]
with open('demo.json','w')as f:
    json.dump(l,f)

my_dict={
    'name':"ayan",
    'student_id' :25001202563


}
with open('demo02.json','w')as f:
    json.dump(my_dict,f,indent=4)   
#deserilizaon
with open('demo02.json','r')as f:
    print(json.load(f)  )


#how serialize class object into json

class person:
    def __init__(self,name,std,gender):
       self.name=name    
       self.std=std 
       self.gender=gender
    
  
per  =person('ayan',12,'male')

#as string
def show_object(per):
    if isinstance(per,person):
        return{
            'name':per.name,
            'std': per.std,
            'gender':per.gender
        }


with open('demo.json','w')as f:
    json.dump(per,f,default=show_object)


