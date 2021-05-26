gauss = 0
sq_sum = 0

for i in range(1, 101):
    gauss += i
    sq_sum += i ** 2

print((gauss ** 2) - sq_sum)
