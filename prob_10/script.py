# used for problem 3, 7 
# pseudo code: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Incremental_sieve
# we use an incremental sieve because memory trade off is too big for my small computer:( 
import sys 

# upper is the number to which primes are calculated 
upper = int(sys.argv[1])

nums = (upper - 1) * [True]
sievebd = int(upper ** (1/2))
int i = 2

while (i < sievebd):
    if nums[i]:
        for j in range(i ** 2, upper, i):
            nums[j] = False

print(nums)
