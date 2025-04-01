#List Operations(nested list,length,concatenation,membership,iteration,indexing,slicing)
list=[[1,2,3],[4,5,6],[7,8,9]]
print(list)
length=(len(list))
print("the length of the list:",length)
list1=[1,2,3]
list2=[4,5,6]
concatenated_list=list1+list2
print(concatenated_list)
print(2 in list1)
print(3 not in list2)
for i in list1:
    print(i)
fruits=['apple','banana','cherry']
x=fruits.index('apple')
print(x)
list=[10,20,30,40,50,60]
print(list[1:5])
