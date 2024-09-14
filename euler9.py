#There exists exactly one Pythagorean triplet for which a + b + c = 1000 . Find the product abd
# a + b + c = 1000
# a**2 + b**2 = c**2

def pythagor(a,b,c):
    if a**2 + b**2 == c**2:
        return(0)
    else:
        return(1)

for i in range(1,1000):
    for k in range(1,1000):
        for l in range(k,1000):
            if i+k+l == 1000 and pythagor(i,k,l) == False:
                print(i,k,l)
                print(i*k*l)