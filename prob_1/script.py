# this baby should be linear time without a lot of space
sum = 0
for i in range(0,1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print(sum)
