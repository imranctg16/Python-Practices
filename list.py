example = []

for i in range(7):
    example.append(i)

for index,element in enumerate(example):
    print(element,index)

#delete an element 
example.remove(3) 

list = [1,2,3,4,4]
print(max(list[0:3+1]))
del example[0] #remove using index