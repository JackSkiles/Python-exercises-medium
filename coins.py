# Creates prompt that asks how many coins a user would like initially.
amount_of_coins = int(input('Please input how many coins you would like: '))

print(amount_of_coins)

# Creates i boolean that is set to False
i = False

# Creates while loop using i that loops until no is entered, adding one coin each
# time yes is entered.
while i == False:
    another_coin = input('Would you like another coin?: ').lower()
    if another_coin == 'yes':
        amount_of_coins += 1
        print(amount_of_coins)
        i = False
    elif another_coin == 'no':
        print('Ok, this is your coin total.')
        break
    else:
        print('Please enter valid input.')
# Prints total amount after loop.
print(amount_of_coins)