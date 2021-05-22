# memory optimized version of generating fibonacci 
fibnums = [1, 2]

def fib_populate(max):
    while(fibnums[-1] < max):
        fibnums.append(fibnums[-1] + fibnums[-2])
fib_populate(4000000)

sum = 0
for i in fibnums: 
    if i % 2 == 0: 
        sum += i
print(sum)  
