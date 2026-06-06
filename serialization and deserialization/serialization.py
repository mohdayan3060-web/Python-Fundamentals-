# if the file is not present 
f=open('shample.txt','w')
f.writelines("heloo the file is created  ")
f.writelines("\nthis is second line ")
f.close()

# f=open('shample.txt','r')
# print(f.read(1))
# f.close()

# f=open('shample.txt','a')
# f.write("\nthis is append mode that do not replace the old content ")
# f.close()


#reading entire file using readline 

f=open('shample.txt','r')
while True:
    data=f.readline()

    if data =='':
        break
    else:
        print(data)

f.close()        


#with

with open('shample01.txt','w') as f:
    f.writelines("\n hey how are you ")
    f.writelines("hey I hope your are doing well")



with open('shample01.txt','r') as f:
    print(f.read())


#smart ways to read very large file 
with open('shample01.txt','w') as f:
    f.write("orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum")


with open('shample01.txt','r') as f:
    chunk_size=10

    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size),end=' ')
        print(f.tell())
        f.seek(0)


#seek and tell
