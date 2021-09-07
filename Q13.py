x= str(input("Enter a string to check : "))
str_1 = ""
for i in x:
    str_1 = i + str_1  
if(x == str_1):
   print("Entered string is a palindrome")
else:
   print("Entered string isn't a palindrome")
