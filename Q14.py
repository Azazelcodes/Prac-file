str1=input("Enter string:")
a=0
d=0
v=0
s=0
c=len(str1)
v1="aeiou"
i=0
while i<c:
    if str1[i].isalpha():
        a=a+1
        if str1[i] in v1:
            v=v+1
    elif str1[i].isdigit():
         d=d+1
    elif str1[i].isspace():
         s=s+1
    i=i+1
print("no of characters", c)
print("no of alphabets", a)
print("no of digits",d)
print("no of vowels", v)
print("no of spaces",s)
