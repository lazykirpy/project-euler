# sum of all the multiples of 3 or 5 below 1000
answer = 0
for _ in range(1000):
    if _%3 == 0 or _%5 == 0:
        answer += _
print(answer)   