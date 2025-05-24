# This program calculates the tax owed based on different tiers of income

import sys

# Define Filing Status Classifications for the user
print('Tax filing status classifications are as follows: \n'\
      ' 0:    Single\n'\
      ' 1:    Married Filing Jointly or Qualified Widow(er)\n'\
      ' 2:    Married Filing Separately\n'\
      ' 3:    Head of Household')

# Prompt the user to enter filing status     
status = int(input("Enter the filing status:"))

# Prompt the user to enter taxable income
income = float(input("Enter the taxable income: "))

# Compute Tax

if status == 0:  # Compute tax for single filers
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 + (income - 372950) * 0.35
elif status == 1: # Compute tax for Married Filing Jointly or Qualified Widow(er)
    if income <= 16700.00:
        tax = income * 0.10
    elif income <= 67900.00:
        tax = (16700.00 * 0.10) + ((income - 16700.00) * 0.15)
    elif income <= 137050.00:
        tax = (16700.00 * .010) + ((67900.00 - 16700.00) * 0.15) + \
            ((income - 67900.00) * 0.25)
    elif income <=  208850.00:
        tax = (16700.00 * 0.10) + ((67900.00 - 16700.00) * 0.15) + \
            ((137050.00 - 67900.00) * 0.25) + ((income - 137050.00) * 0.28)
    elif income <= 372950.00:
        tax = (16700.00 * 0.10) + ((67900.00 - 16700.00) * 0.15) + \
            ((137050.00 - 67900.00) * 0.25) + ((208850.00 - 137050.00) * 0.28) + \
            ((income - 208850.00) *  0.33)
    else:
        tax = (16700.00 * 0.10) + ((67900.00 - 16700.00) * 0.15) + \
            ((137050.00 - 67900.00) * 0.25) + ((208850.00 - 137050.00) * 0.28) + \
            ((372950.00 - 208850.00) * 0.33) + ((income - 372950.00) * 0.35)
elif status == 2: # Compute tax for Married Filing Separately
    if income <= 8350.00:
        tax = income * 0.10
    elif income <= 33950.00:
        tax = (8350.00 * 0.10) + ((income - 8350.00) * 0.15)
    elif income <= 68525.00:
        tax = (8350.00 * 0.10) + ((33950.00 - 8350.00) * 0.15) + \
            ((income - 33950.00) * 0.25)
    elif income <= 104425.00:
        tax = (8350.00 * 0.10) + ((33950.00 - 8350.00) * 0.15) + \
              ((68525.00 - 33950.00) *  0.25) + ((income -  68525.00) * 0.28)
    elif income <= 186475.00:
        tax = (8350.00 * 0.10) + (( 33950.00 - 8350.00) * 0.15) + \
              ((68585.00 - 33950.00) * 0.25) + ((104425.00 - 68525.00) * 0.28) +\
              ((income - 104425.00) * 0.33)
    else:
        tax = (8350.00 * 0.10) + ((33950.00 - 8350.00) * 0.15) + \
              ((68525.00 - 33950.00) * 0.25) + ((104425.00 - 68525.00) * 0.28) +\
              ((186475.00 - 104425.00) * 0.33) + ((income - 186475.00) * 0.35)
elif status == 3: # Compute tax for Head of Household
    if income <= 11950.00:
        tax = income * 0.10
    elif income <= 45500.00:
        tax = (11950.00 * 0.10) + ((income - 11950.00) * 0.15)
    elif income <= 117450.00:
        tax = (11950.00 * 0.10) + ((45500.00 - 11950.00) * 0.15) + \
              ((income - 45500.00) * 0.25)
    elif income <= 190200.00:
        tax = (11950.00 * 0.10) + ((45500.00 - 11950.00) * 0.15) + \
              ((117450.00 - 45500.00) * 0.25) + ((income - 117450.00) * 0.28)
    elif income <= 372950.00:
        tax =  (11950.00 * 0.10) + ((45500.00 - 11950.00) * 0.15) + \
              ((117450.00 - 45500.00) * 0.25) + ((190200.00 - 117450.00) * 0.28) +\
              ((income - 190200.00) * 0.33)
    else:
        tax = (11950.00 * 0.10) + ((45500.00 - 11950.00) * 0.15) + \
              ((117450.00 - 45500.00) * 0.25) + ((190200.00 - 117450.00) * 0.28) +\
              ((372950.00 - 190200.00) * 0.33) + ((income - 372950.00) * 0.35)

else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", tax)
