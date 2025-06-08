def read_and_format_triangle(file_path, base_width=1):
    triangle = []

    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            triangle.append(row)

    max_row_length = len(triangle[-1])
    output_lines = []

    for i, row in enumerate(triangle):
        # Calculate width for this row's elements
        element_width = base_width + 2 * i
        # Format each number
        formatted_numbers = [str(num).center(element_width) for num in row]
        # Join numbers into a string
        row_str = ' '.join(formatted_numbers)
        # Calculate total row width
        total_row_width = (element_width + 1) * max_row_length - 1
        # Center the row
        centered_row = row_str.center(total_row_width)
        output_lines.append(centered_row)
    return output_lines

lines = read_and_format_triangle("Maximum_Path_Sum_1.txt")
for line in lines:
    print(line)
