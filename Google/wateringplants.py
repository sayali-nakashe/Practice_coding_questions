plants = [2, 4, 5, 1, 2]
capacity = 6

temp_cap = 6
steps = 0
for i in range(len(plants)):
    if (capacity < plants[i]):
        steps = 0
    if temp_cap<plants[i]:
        steps+= 2*i
        temp_cap = capacity - plants[i]
    else:
        temp_cap-=plants[i]
    steps+=1

print(steps)


