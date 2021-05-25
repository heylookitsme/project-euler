#19 is our biggest prime guys. we can just find multiples of 19 

# get a lot of multiples of 19, since it is the biggest prime. the list is not actually short 
shortlist = [x * 19 for x in range(1000000, 100000000) if (x % 20 == 0 and x % 17 == 0 and x % 13 == 0 and x % 11 == 0)]

print([x for x in shortlist if is_div(x)])

# checks if the number is a valid one
def is_div(num): 
    res = True 
    for i in range(1, 20): 
        if num % i != 0 
            res = False 
            break
    return res
