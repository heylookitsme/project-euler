# we brute force factors of the given number, since there are only sqrt(num) = 700k iterations to find all factors. not bad.
num = 600851475143
factors = [1, num]

for i in range(2, int(num ** (1/2)) + 1):
    if num % i == 0:
        factors.append(i)

print(factors)
