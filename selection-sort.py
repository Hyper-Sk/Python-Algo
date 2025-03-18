
# Example with pop and insert method 

myArray = [5,4,3,0,1,2,6]

arrLen = len(myArray)

for i in range(arrLen - 1):
    
    for j in range(i,arrLen):
        if myArray[j] < myArray[i]:
            popedItem = myArray.pop(j)
            myArray.insert(i,popedItem)

# print(myArray)



# Example with list item swaping. 


myArray2 =  [5,4,3,0,1,2,6,7,9]

arr2Len = len(myArray2)

for i in range(arr2Len - 1):
    for j in range(i,arr2Len):
        if myArray2[j] < myArray2[i]:
            myArray2[j],myArray2[i] = myArray2[i],myArray2[j] 

print(myArray2)