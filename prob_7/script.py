# hello and welcome to prime farming simulator. how many primes would you like to farm today- 
# oh? 10001? that is a lot of primes sir D: uhhh give us a second

# hi guys today we'll be making an "okay" prime sieve. it is like you are panning for primes the same way 
# you would pan for gold, but instead of a river youre panning the natural numbers and instead of a pan
# you have a computer and python

# we will modify the pseudo code for the sieve of erathostanes but modified from wikipedia because i am bad at math: 
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#    input: an integer n > 1.
#    output: all prime numbers from 2 through n.
#
#    let A be an array of Boolean values, indexed by integers 2 to n,
#    initially all set to true.    
#
#    for i = 2, 3, 4, ..., not exceeding √n do
#        if A[i] is true
#            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                A[j] := false
#    return all i such that A[i] is true.

found_primes = [2]
curr = 2

# this runs for so long. 
while (len(found_primes) != 10001):
    for i in found_primes:
        if curr % i == 
