# sum of even valued fibonacci numbers below 4,000,000
# fib numbers is:F1=F2=1, F1 +F2 = F3, F2+F3= F4 and so on
a, b = 0, 1  
numlist=[]
n = 4000000

while b < n:
    if b%2==0:
        numlist.append(b)

    a, b = b, a+b
answer = 0 
for i in numlist:
    answer += i
print(answer)