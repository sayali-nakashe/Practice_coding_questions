plants = [2, 4, 5, 3, 2]
cap1 = 6
cap2 = 4

tcap1 = cap1
tcap2 = cap2
steps1 = 0
steps2 = 0

i = -1
while j-i!=2:
    
    i+=1
    j = len(plants)-i-1
    
    if (cap1 < plants[i]) and (cap2 < plants[j]):
        steps = 0
    print("i : ",plants[i])
    print("j : ",plants[j])
    
    print("tcap1 : ",tcap1)
    if tcap1 < plants[i]:
        steps1+= 2*i
        tcap1 = cap1 - plants[i]
    else:
        tcap1-=plants[i]
        steps1+=1
    print("tcap1 steps : ",steps1)
    print("after tcap1 : ",tcap1)
    print("\n-------------------------\n")
    print("tcap2 : ",tcap2)
    if tcap2 < plants[j]:
        print("yes : ",2*(len(plants)-(j+1)))
        steps2+= 2*(len(plants)-(j+1))
        tcap2 = cap2 - plants[j]
    else:
        tcap2-=plants[j]
        steps2+=1
    print("tcap2 steps : ",steps2)
    print("after tcap2 : ",tcap2)
    print("\n-----------------------\n")
 
print("i: ",i)
print("j : ",j)
if(i+1==j-1):
    if(tcap1>plants[i+1] or tcap2>plants[j-1]):
        steps1+=1
    else:
        steps1+=2*(i+1)

print("Final steps 1 : ",steps1)
print("Final steps 2: ",steps2)


