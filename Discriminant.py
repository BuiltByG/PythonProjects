# Prompt the user to enter the discriminant values:
print('Enter the discriminant values:')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

# Define the formula for finding the discriminant
discriminant = (b ** 2) - (4 * (a * c))
if discriminant > 0:
    print('The equation has two roots!')
elif discriminant == 0:
    print('The equation has one root!')
else:
    print('The equation has no real roots.')
