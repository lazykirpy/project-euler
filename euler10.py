#Find the sum of all the primes below two million.
from math import sqrt
i=2
numlist=[]
answer=0
def isPrime(i):
    div = 2
    while div <= sqrt(i):
        if i%div == 0:
            return(1)
        else:div+=1
    #remove this print if you just want the answer
    print(f"{i} is a prime")
    numlist.append(i)

while i<2000000:
    isPrime(i)
    i+=1
for i in numlist:
    answer += i
print(answer)