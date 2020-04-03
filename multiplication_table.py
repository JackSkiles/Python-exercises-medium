# Creates number variable to count and multiply with.
num = 1

num2 = 1

num3 = 1

# Creates a while loop that loops through as long as 4 is less than 10. Each loop multiplies the other three numbers and prints out the changing results.
num4 = 0
while num4 < 10:
    num3 = num * num2
    print(f'{num} X {num2} = {num3}')
    num4 += 1
    num += 1
    num2 += 1


    