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

#get last element from list 

str = "Mohammad Imran Hossain"
print(str.split()[-1])

# merge 
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1[:] = nums1[:m] + nums2