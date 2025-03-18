# fibonacci algorithum using loop 

prev1 = 0
prev2 = 1

# print(prev1)
# print(prev2)
for i in range(16):
    newFibonacci = prev1 + prev2
    # print(newFibonacci)
    prev1 = prev2
    prev2 = newFibonacci








# fibonacci using rescursion 
    
# print(0)
# print(1)
count = 1

def fibonacci(prev1,prev2):
    global count
    if count <= 15:
        newFibo = prev1 + prev2
        print(newFibo)
        prev1 = prev2
        prev2 = newFibo
        count += 1
        fibonacci(prev1,prev2)
    else:
        return
    

# fibonacci(0,1)






# fibonacci using formula 
    
    # formula : f(n) = f(n-1) + f(n-2)

def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
    
print(F(19))
