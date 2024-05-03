#https://projecteuler.net/problem=2

def generateFibonacci():
    a = 1
    b = 2    
    def generator():
        nonlocal a
        nonlocal b
        temp = a
        a,b = b,a+b               
        return temp
    
    return generator

# call this function to find the final answer 
def findSum():
    f = generateFibonacci()
    sum_val = 0
    while True:
        v = f()
        if v > 4000000:
            break
        
        if v % 2 == 0:
            sum_val += v
    
    return sum_val
