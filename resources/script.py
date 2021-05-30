# https://www.codevamping.com/2019/01/incremental-sieve-of-eratosthenes/


# used for problem 3, 7 
# pseudo code: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Incremental_sieve
# we use an incremental sieve because memory trade off is too big for my small computer:( 
import sys 

# upper is the number to which primes are calculated 
upper = int(sys.argv[1])

nums = (upper - 1) * [True]
sievebd = int(upper ** (1/2))
i = 2

while (i < sievebd):
    if nums[i]:
        for j in range(i ** 2, upper - 1, i):
            nums[j] = False
    i += 1

res = []
for i in range(0, len(nums)):
    if nums[i]:
        res.append(i + 3)

print(res)
