import math
import csv

# variables
last_to_check = 1000000
numbers_checked = []
ratios = []
list_of_lengths = []
lowest_ratios = []

# does process described in the video


def collatz(input):
    length = 0
    number = input
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            length += 1
        elif number % 2 == 1:
            result = 3 * number + 1
            number = result
            length += 1

    # appends values to the lists
    list_of_lengths.append(length)
    ratios.append(math.log2(input)/length)
    numbers_checked.append(input)


# actually excecutes the process for all numbers
for i in range(2, last_to_check):
    collatz(i)

# generates csv file
with open("collatz_lengths.csv", "w") as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(numbers_checked)
    csv_writer.writerow(list_of_lengths)
    csv_writer.writerow(ratios)

# finds new lowest ratios
current_lowest_ratio = 1
for i in ratios:
    if i < current_lowest_ratio:
        current_lowest_ratio = i
        lowest_ratios.append(numbers_checked[ratios.index(i)])

print(lowest_ratios)
