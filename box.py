
# Asks user for input to decide the square's height and width
square_height = int(input('Please input how tall you would like your square to be'))

square_width = int(input('Please input how wide you would like your square to be.'))

# Creates a counter to increment line breaks for the height portion
counter = 0
# Creates an empty string that will be filled with line breaks and *'s
square_creator = ''

# Forms the loop that goes for however long the input sepecified. Looping through the width portion each time 
# there is a line break.
while counter < square_height:
    counter2 = 0
    while counter2 <= square_width:
        square_creator += ' '
        counter2 += 1
    print('*')
    counter += 1
print(square_creator)
