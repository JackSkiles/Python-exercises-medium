
# Asks user to input their intial bill and party size.
amount_of_people = input('How many people are in your party?: ')
amount_of_people = float(amount_of_people)

bill = input('What was your total bill amount?: ')
bill = float(bill)

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

# Divides the total bill by amount of party members for each person's bill.
party_split = total_bill / amount_of_people

print(f'Your total bill per person is {party_split}')