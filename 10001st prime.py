from time import sleep
primes = [2]
i=3
def isPrime(n,primes):
    for i in range(len(primes)):
        if(n%2 == 0):
            return False
        if(n%primes[i]==0):
            return False
    return True
while(True):
    if(isPrime(i,primes)):
        print(len(primes))
        primes.append(i)
    if(len(primes)==10001):
        print(primes[10000])
        sleep(20)
    i=i+1
