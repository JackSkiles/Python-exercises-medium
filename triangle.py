
# Creates triangle variable to edit
triangle = ''

# Creates counter
triangle_count = 0
 # Creates while loop that increments 5 times to check if the condditions of the if statements are met. The if statements run 5 times and print their corrisponding
 # text to complete the triangle.
while triangle_count < 5:
    if triangle_count == 0:
        triangle += '    *    \n'
        #print(triangle)
    elif triangle_count == 1:
        triangle += '   ***   \n'
        #print(triangle)
    elif triangle_count == 2:
        triangle += '  *****  \n'
        #print(triangle)
    elif triangle_count == 3:
        triangle += ' ******* \n'
        #print(triangle)
    else:
        print(triangle)
    triangle_count += 1


