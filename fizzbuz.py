

number = int(input('Please enter an integer you would like to go to: '))

counter = 1

while counter <= number:
    if counter % 3 == 0 and counter % 5 == 0:
        print('fizzbuzz')
    elif counter % 3 == 0:
        print('fizz')
    elif counter % 5 == 0:
        print('buzz')
    else:
        print(counter)
    counter += 1