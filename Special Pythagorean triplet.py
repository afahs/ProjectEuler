from operator import mul
def triple(m,n):
    a = m**2-n**2
    b = 2*m*n
    c = m**2+n**2
    return [a,b,c]
for i in range(23):
    for j in range(23):
        z=triple(i,j)
        print(z)
        if(sum(z)==1000):
          print(mul(z))  
