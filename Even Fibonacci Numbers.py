def fib(n):
    return round((1/5**0.5)*((1+5**0.5)/2)**n)
evenFib = []
for i in range(3,34,3):
    evenFib.append(fib(i))
print(evenFib)
print(sum(evenFib))
