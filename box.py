square_height = int(input('Please input how tall you would like your square to be'))

square_width = int(input('Please input how wide you would like your square to be.'))

# Creates a counter to increment line breaks for the height portion
counter = 0
# Creates an empty string that will be filled with line breaks and *'s
square_creator = ''
# A second counter to be used later on
counter2 = 0
# Creates an if statement to check if it is the first line. If it is it procedes with the loop to add a line  of *'s based on user input.
if counter == 0:
    while counter <= square_width:
        square_creator += ' * '
        counter += 1
    square_creator += '\n'

# Using a second and third counter these nested loops add * and empty spaces every row based on user input. After the nested loop runs a * and line break occurs and then another * is printed
# on the start of the outer loop.
while counter2 <= square_height:
    counter3 = 0
    square_creator += ' * '
   
    while counter3 <= square_width:
        square_creator += '  '
        counter3 += 1
    square_creator += ' *\n'
    counter2 += 1
# Using a fourth counter mimics the start of the box and prints a straight line of * based on user input.
counter4 = 0

if counter4 == 0:
    while counter4 <= square_width:
        square_creator += ' * '
        counter4 += 1
print(square_creator)

