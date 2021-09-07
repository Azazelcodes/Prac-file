maxi = int(input("Enter the maximum value/ the last value/ value of n : "))
even_tot= 0
odd_tot= 0
for number in range(1, maxi + 1):
    if(number%2==0):
        even_tot=even_tot+number
    else:
        odd_tot=odd_tot+number
print("The sum of even numbers from 0 to", number,"is:",even_tot)
print("The sum of odd numbers from 0 to", number,"is:", odd_tot)
