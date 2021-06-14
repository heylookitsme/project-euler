# yes, i know, dp solution is better
# brute force solution 
# sosqd = sum of square digits
def find_sosqd(num):
    sum = 0 
    while(num != 0):
        sum += (num % 10) ** 2
        num = num // 10
    return sum

ends_at_89 = []
for i in range(1, 10000000):
    temp = i
    while(temp != 1 and temp != 89):
        temp = find_sosqd(temp)
    if temp == 89: 
        ends_at_89.append(i)
print(len(ends_at_89))
