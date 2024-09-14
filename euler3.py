#largest prime factor of 600851475143
from math import sqrt
factors=[]
notprimes=[]
def isaPrime(i):
    limit,n=sqrt(i),2
    while n<=limit:
        if i%n == 0:
            factors.append(n)
        n+=1
num = input("Input a valid number: ")
isaPrime(int(num))
for i in factors:
    limit,n=sqrt(i),3
    while n<=limit:
        if i%n == 0:
            notprimes.append(i)
            break
        n+=2
for i in notprimes:
    for j in factors:
        if i == j:
            factors.remove(j)
print(f"Prime factors: {factors}")