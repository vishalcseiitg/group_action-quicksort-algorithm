def eligible_pivot(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r') as file:
        # Read the contents of the file into a list of integers
        arr = [int(line.strip()) for line in file]

    n = len(arr)
    eligible = []
    for i in range(n):
        is_eligible = True
        for j in range(n):
            if i != j and arr[i] >= arr[j]:
                is_eligible = False
                break
        if is_eligible:
            eligible.append(arr[i])

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Write the eligible pivot elements to the output file
        file.write('\n'.join(map(str, eligible)))

# Call the function with input and output file paths
eligible_pivot('input.txt', 'output.txt')
