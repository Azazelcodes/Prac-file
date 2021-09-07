n=int(input("Enter number to check for Palindrome:"))
temp=n
revs=0
while(n>0):
    digi=n%10
    revs=revs*10+digi
    n=n//10
if(temp==revs):
    print("Entered number is a palindrome")
else:
    print("Entered number ain't a palindrome")
