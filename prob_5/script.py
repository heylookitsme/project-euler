# we write this solution for people who are not particularily good with primes and number theory (me), 
# but are just smart enough to know a little bit about factors. there is a much smarter solution 
# that actually involves thinking and is the first post on the project euler forum (by bitRAKE). 
# 
# however, note: due to the nature of this brute force answer, the while loop will run like ~12 million times, 
# and probably due to the way python does ranges/functions, this program eats up precious memory, and 
# hence a different method than brute force is highly preffered. 
#
# that being said, the strategy here is this: since 19 is the biggest prime, we will only look at numbers 
# that are a multiple of 19 (in hindsight, it wouldnt matter if 20 was the multiple but oh well). for 
# each of those multiples, the function is_div checks if the number is divisible by numbers from 1 - 19 
# (in hindsight, redundant). then, once the first number which satisfies is_div is found, the loop stops 

curr = 2520 # we use this as a lower bound because we know this guy is divisible from 1 to 10 
j = 2520 // 19

# checks if a given number is divisible by numbers in the range 1 - 20 
def is_div(num):
    res = True
    print(curr)
    for i in range(1,20):
        if num % i != 0:
            res = False
            break
    return res

while(not is_div(curr)):
    curr = 19 * j
    j += 1

print(curr)
print(j)

