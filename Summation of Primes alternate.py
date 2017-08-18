n = 2000000
numbers = [True]*n
SumPrimes = 0
for i in range(2,round(n**0.5)+1):
    if(numbers[i]==True):
        for j in range(2*i,n,i):
            numbers[j] = False
for i in range(2,len(numbers)):
    if(numbers[i]==True):
        SumPrimes+=i
print(SumPrimes)

