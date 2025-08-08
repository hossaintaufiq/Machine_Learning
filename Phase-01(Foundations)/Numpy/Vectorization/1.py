list1=[1,2,3,4,5,6,7,8]

list2=[10,20,30,2,3,5]

result= [x+y for x,y in zip(list1, list2)]

print(result)  # Output: [11, 22, 33, 6, 8, 11, 15, 10]
