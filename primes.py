x = int(input("Enter a number to print all the primes : "))
for i in range(2,x):
    count = 0
    for j in range(2,int(i/2)+1):
        if(i%j == 0):
            count+=1
    if count == 0:
        print(i,end=' ')