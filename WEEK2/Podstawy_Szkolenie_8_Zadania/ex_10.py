
def get_ints_from_file_str(name_file):
    with open('dane.txt', 'r') as image_file:
        image_line = image_file.readlines()
        image_values = []

        for i in range(len(image_line)):
            temp_image_values = image_line[i].split(" ")

            for j in range(len(temp_image_values)):
                temp_image_values[j] = int(temp_image_values[j])

            image_values.extend([temp_image_values])
        return image_values


def find_min_and_max(values):
    current_max_val = 0
    current_min_val = 0

    for k in range(len(values)):
        max_val = max(values[k])
        min_val = min(values[k])

        if max_val > current_max_val: current_max_val = max_val
        if min_val < current_min_val: current_min_val = min_val

    print(f'Min value: {current_min_val}')
    print(f'Max value: {current_max_val}')


def find_axis_of_symmetry(values_list):
    symmetric_lines = []

    for i in range(len(values_list)):
        symmetric_count = 0
        pixels = len(values_list[i])
        half_pixels = int(len(values_list[i])/2)

        for j in range(half_pixels):
            if values_list[i][j] == values_list[i][pixels-j-1]:
                symmetric_count += 1

        symmetric_lines.append(symmetric_count)
    return symmetric_lines.count(0)


def has_contrasting_neighbor(pixel, neighbors):
    for neighbor in neighbors:
        if abs(pixel - neighbor) > 128:
            return True
    return False


def count_pixels_with_contrasting_neighbors(pixel_values):
    row_amount = len(pixel_values)
    pixel_amount = len(pixel_values[0])
    count = 0

    for i in range(row_amount):
        for j in range(pixel_amount):
            pixel = pixel_values[i][j]
            neighbors = []
            if i > 0:
                neighbors.append(pixel_values[i - 1][j])
            if i < row_amount - 1:
                neighbors.append(pixel_values[i + 1][j])
            if j > 0:
                neighbors.append(pixel_values[i][j - 1])
            if j < pixel_amount - 1:
                neighbors.append(pixel_values[i][j + 1])

            if has_contrasting_neighbor(pixel, neighbors):
                count += 1

    return count


def find_longest_vertical_line(image_values_list):
    row_amount = len(image_values_list)
    pixel_amount = len(image_values_list[0])
    longest_line = 0

    for j in range(pixel_amount):
        current_line_length = 1
        for i in range(1, row_amount):
            if image_values_list[i][j] == image_values_list[i - 1][j]:
                current_line_length += 1
            else:
                current_line_length = 1

            longest_line = max(longest_line, current_line_length)

    return longest_line


image_values_list = get_ints_from_file_str('dane.txt')

find_min_and_max(image_values_list)

print(f'Rows to delete: {find_axis_of_symmetry(image_values_list)}')

count_contrasting_pixels = count_pixels_with_contrasting_neighbors(image_values_list)
print(f'Contrasting pixels: {count_contrasting_pixels}')

longest_line = find_longest_vertical_line(image_values_list)
print(f'Longest vertical line: {longest_line}')
