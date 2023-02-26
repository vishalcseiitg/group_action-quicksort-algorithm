import random

start_range = 1  # start of range
end_range = 10000000  # end of range
output_file_name = "distinct_numbers.txt"

# create a set of all numbers in the range
all_numbers = set(range(start_range, end_range+1))

# shuffle the set to make the order random
shuffled_numbers = list(all_numbers)
random.shuffle(shuffled_numbers)

# write the shuffled numbers to the output file
with open(output_file_name, 'w') as output_file:
    for number in shuffled_numbers:
        output_file.write(str(number) + "\n")

print("File generated successfully!")

