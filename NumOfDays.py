# Prompt the user to enter the month and year
month = int(input('Enter the month (i.e. May = 5, June = 6 etc.): '))
year = int(input('Enter the year: '))


def days (m, y):
    if month == 1:
        print('31')
    elif month == 2 and year % 100 != 0 and year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
        print('29')
    elif month == 2 and year % 100 != 0 and year % 4  != 0 or year % 100 == 0 and year % 400 != 0:
        print('28')
    elif month == 3:
        print('31')
    elif month == 4:
        print('30')
    elif month == 5:
        print ('31')
    elif month == 6:
        print('30')
    elif month == 7:
        print('31')
    elif month == 8:
        print('31')
    elif month == 9:
        print('30')
    elif month == 10:
        print('31')
    elif month == 11:
        print('30')
    elif month == 12:
        print('31')
print('Number of days: ', end = ' ')
days (month, year)
