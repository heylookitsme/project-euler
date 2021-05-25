max_1 = 0 
max_2 = 0
max_comp = 0

# "guessed" range
for i in range(999, 500, -1): 
    for j in range(i, 500, -1):
        comp = i * j
        if (comp > max_comp and str(comp) == str(comp)[::-1]):
            max_1 = i
            max_2 = j
            max_comp = comp
    
print(max_1)
print(max_2)
print(max_1 * max_2)
