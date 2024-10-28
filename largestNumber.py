#learn how to print largest number in a list

numbers = [5, 6 , 8, 7, 2, 1, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

