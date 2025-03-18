myArray = [1,5,4,3,2,0]

arrLen = len(myArray)

for i in range(1,arrLen):
    insert_index = 1
    current_value = myArray.pop(i)
    # -1 in third parameter is used to reverse the range 
    for j in range(i-1,-1,-1):
        if myArray[j] > current_value:
            insert_index = j
            # print(j)
    # myArray.insert(insert_index,current_value)

print(myArray)
        
