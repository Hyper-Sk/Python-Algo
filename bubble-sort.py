myArray = [5,3,4,2,5,6,3,1]

arrLen = len(myArray)
# print(arrLen)
for i in range(arrLen-1):
    for j in range(arrLen-i-1):
        if myArray[j] > myArray[j+1]:
            # here we are swaping list item values 
            myArray[j],myArray[j+1] = myArray[j+1],myArray[j]
print('Bubble Sorted Array : ',myArray)