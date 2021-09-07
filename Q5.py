num=(int(input("Enter no. to be reversed:")))
rev=0
while(num > 0):
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
 
print(rev)
