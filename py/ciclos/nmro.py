print("""determonar que numeros del 1 al 1000 son perfectos""""")
for n in range (1,1001):
    s=0
    for i in range (1,n):
        if n%i==0:
            print("divisor",i)
            s=s+i 
    if s==n:
        print("perfecto",n)
    else:
        print("no perfecto")