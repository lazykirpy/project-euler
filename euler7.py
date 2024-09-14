from math import sqrt

i=2
numlist=[]
def isPrime(i):
    div = 2
    while div <= sqrt(i):
        if i%div == 0:
            return(1)
        else:div+=1
    #remove this print if you just want the answer

    numlist.append(i)

while len(numlist)< 10001:
    isPrime(i)
    i+=1
print(numlist[-1])