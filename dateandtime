



from datetime import datetime
import time

odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

condition = input('What is your current condition? ')

for i in range(5):
    right_this_minute = datetime.today().minute

    today = datetime.today().day

    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    if today == 5:
        print('Party!!')
    elif today == 6:
        if condition == 'headache':
            print('Recover!')
        elif condition == 'fine':
            print('Proceed!')
    else:
        print('Work, work, work.')
