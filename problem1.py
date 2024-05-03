# https://projecteuler.net/problem=1

def findSum():
    sum_val = 0
    
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_val += i
    
    return sum_val
