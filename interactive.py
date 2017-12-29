

from datetime import datetime
import time

date = datetime.today().day
time = datetime.today().now()
name = input('Hello, who am I working with today? ')

print('\n' + 'Great to see you ' + name.capitalize() + '!' + ' Let\'s get some work done.')

if date == 'Monday':
    print('Today is Monday and it is currently ' + time.strftime("%H:%M"))
elif date == 'Tuesday':
    print('Today is Tuesday and it is currently ' + time.strftime("%H:%M"))
elif date == 'Wednesday':
    print('Today is Wednsday and it is currently ' + time.strftime("%H:%M"))
elif date == 'Thursday':
    print('Today is Thursday and it is currently ' + time.strftime("%H:%M"))
elif date == 'Friday':
    print('Today is Friday and it is currently ' + time.strftime("%H:%M"))
elif date == 'Saturday':
    print('Today is Saturday and it is currently ' + time.strftime("%H:%M"))
else:
    print('Today is Sunday and it is currently ' + time.strftime("%H:%M") + '.')
