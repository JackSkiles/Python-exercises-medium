
# Asks user to input their intial bill.
bill = int(input('What was your total bill amount?: '))

# Creates an i variable and sets it to false to use in a while loop.
i = False

# Creates a loop that will continue until the user uses a correct promt. When they do it returns a tip amount based on the prompt they gave.
while i == False:
    level_of_service = input('Enter level of service. enter either good, fair or bad?: ')
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

# Multiplies the tip amount and bill to come up with a tip total.
tip_total = bill * tip_amount

# Adds the tip total to bill under a new variable for the total bill.
total_bill = bill + tip_total

print(f'Your total bill is {total_bill}')