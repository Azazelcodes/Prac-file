num = int(input('How many numbers to add: '))
total = 0
 
for n in range(num):
    numbers = float(input('Enter 1 number : '))
    total += numbers
 
avg = total/num
print('The average of entered ', num, ' numbers is :', avg)
