n=int(input("Enter a number whose digits are to be added:"))
totl=0
while(n>0):
    digi=n%10
    totl=totl+digi
    n=n//10
print("The total sum of digits is:",totl)
