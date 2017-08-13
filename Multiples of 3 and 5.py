mult3 = []
mult5 = []
for i in range(1,334):
    mult3.append(3*i)

for i in range(1,200):
    mult5.append(5*i)

for i in range(len(mult3)-1):
    if(mult3[i]%15==0):
        mult3[i]=0
ans = sum(mult3)+sum(mult5)
print(ans)
