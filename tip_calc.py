

total_bill = int(input('What was your total bill amount? '))

#level_of_service = input('Please enter level of service. enter either good, fair or bad')

#level_of_service = level_of_service.lower()

tip_amount = 0.0

i = False

while i == False:
    level_of_service = input('Enter level of service. enter either good, fair or bad')
    level_of_service = level_of_service.lower()
    if level_of_service == 'good':
        tip_amount = .2
        i = True
    elif level_of_service == 'fair':
        tip_amount = .15
        i = True
    elif level_of_service == 'bad':
        tip_amount = .1
        i = True
    else:
        print('Please enter a valid service rating.')
        i = False
print(tip_amount)