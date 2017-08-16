primes = [2]
i=3
sump = 2
def isPrime(n,primes):
    for i in range(len(primes)):
        if(n%primes[i] == 0):
            return False
    return True
while(i<2000001):
    if(isPrime(i,primes)):
        primes.append(i)
        print(len(primes))
        sump += i
    i += 2
print(sump)
