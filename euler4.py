#largest palindrome made from  product of two 3digit nummbers ex:9009=91x99
#my solution is a palindrome checker.
pals = []
def palchecker(a):
    c = str(a)
    b = int(len(c)/2)
    pal1 = c[:b]
    pal2 = c[b:][::-1] 
    if pal1 == pal2:
        print("is a pal")
        pals.append(a)
for i in range(800,999):
    for j in range(800,999):
        palchecker((i*j))
pals.sort()
print(pals)