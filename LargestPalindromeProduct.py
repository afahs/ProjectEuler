list = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        pal = i*j
        pal = str(pal)
        if(pal==''.join(reversed(pal))):
            list.append(int(pal))
print(max(list))
