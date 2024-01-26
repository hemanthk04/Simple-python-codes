st1 = input("Enter a number to check palindrome : ")
s1 = len(st1)
count =int(0)
for i in range(s1):
    if(st1[i] != st1[-i-1]):
        count = count+1
if (count==0):
    print("Palindrome")
else:
    print("not a palindrome")