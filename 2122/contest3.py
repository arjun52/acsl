 the parameter is the nth number in teh fib seq, so get the nth row of the triangle and the [0] (should be 1) and keep going to the previous row and [x+1] until it ends

from math import factorial
nth = 1
w = 1
e = 1
r = 1
t = 0
fibNumber = 21
while nth == 1:
    r = w + e
    if fibNumber == r:
        nth = t + 2
    w = e
    e = r
    t += 1
nth += 1

n = nth #n is the nth number of the fib seq
lanif = [] # final list of diagonals
while n > 0:
   
    y = 2 # changing number for getting the diagonals
    z = 0 # changing increment of the diagonal
    
    x = int(((n**2)/2)+1-n/2) # x is the # of the first number of nth line of the pascals triangle
    nn = int(n/2)
    if ".5" in str(nn):
        nn = int(nn + 0.5)
    X = x-1 #X is the index number of x, so it will be x-1
    pascals = [] #pascals triangle
    for a in range(n):
        for b in range(a+1): 
            pascals.append(factorial(a)//(factorial(b)*factorial(a-b)))
    #print(pascals)
    lanif.append(pascals[X])
    for i in range(0,nn):
        lanif.append(pascals[(X)-(n-2-z)])
        #print(lanif)
        X = (X)-(n-2-z) # does recursion so that it will be X - j, X - j + 1, X - j + 2, etc
        z += 1
    n += -1
#print(f'all of the diagonals are {lanif}')
unique = 0
for x in lanif:
    if lanif.count(x) == 1:
        unique += 1 
print(unique)
