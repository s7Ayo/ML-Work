source_grid = [
    [3, 0, 1, 5, 0, 3, 0, 3],
    [2, 6, 2, 4, 3, 0, 3, 0],
    [2, 4, 1, 0, 6, 1, 4, 1],
    [3, 0, 1, 5, 0, 3, 0, 2],
    [2, 6, 2, 4, 3, 2, 3, 0],
    [2, 4, 1, 0, 6, 2, 1, 1],
    [2, 6, 2, 4, 4, 0, 3, 6],
    [2, 4, 1, 0, 6, 1, 6, 1]
]

# Filter 
filter_ = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

# Function to apply the filter to a 3x3 region of the source image
def apply_filter(region, filter_):
    return sum(region[i][j] * filter_[i][j] for i in range(3) for j in range(3))

# Apply the filter to each 3x3 block in the source image to create the 6x6 output image
output_image = []
for i in range(len(source_grid) - 2):
    output_row = []
    for j in range(len(source_grid[i]) - 2):
        # Extract the 3x3 region
        region = [row[j:j+3] for row in source_grid[i:i+3]]
        # Apply the filter to the region
        filtered_value = apply_filter(region, filter_)
        output_row.append(filtered_value)
    output_image.append(output_row)

print(output_image)
