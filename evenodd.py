list1=[1,2,3,4,5,6,7,8,9]
even,odd=0,0
for num in list1:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
 
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)