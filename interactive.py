

from datetime import datetime
import time

date = datetime.today().weekday()
time = datetime.today().now()
name = input('Hello, who am I working with today? ')

print('\n' + 'Great to see you ' + name.capitalize() + '!' + ' Let\'s get some work done.')

if date == '0':
    print('Today is Monday and it is currently ' + time.strftime("%H:%M"))
elif date == '1':
    print('Today is Tuesday and it is currently ' + time.strftime("%H:%M"))
elif date == '2':
    print('Today is Wednsday and it is currently ' + time.strftime("%H:%M"))
elif date == '3':
    print('Today is Thursday and it is currently ' + time.strftime("%H:%M"))
elif date == '4':
    print('Today is Friday and it is currently ' + time.strftime("%H:%M"))
elif date == '5':
    print('Today is Saturday and it is currently ' + time.strftime("%H:%M"))
else:
    print('Today is Sunday and it is currently ' + time.strftime("%H:%M") + '.')
