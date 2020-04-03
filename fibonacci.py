main_numb = int(input('Please input a number to end on: '))


num = 0
num2 = 1


counter = 0

new_numb = 0
while counter < main_numb:
    new_numb = num + num2
    print(new_numb)
    num = new_numb
    num2 = num - num2
    counter += 1
