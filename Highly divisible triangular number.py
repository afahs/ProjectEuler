def numDivisors(n):
    divisors = []
    for i in range(1,round(n**0.5+1)):
        if(n%i == 0):
            if(n/i == i):
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n/i)
    return len(divisors) 
number = 0
i=1
while(numDivisors(number)<=500):
    number+=i
    print(numDivisors(number))
    i+=1
print(number)
