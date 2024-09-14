sum=0
sqrsum=0
for i in range(1,101):
    sum+=i
    sqrsum+= i * i
sum = sum*sum
answer = sum-sqrsum
print(answer)