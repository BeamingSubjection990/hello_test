# This is a simple Python program that calculates the area of a rectangle

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    :param length: float, the length of the rectangle
    :param width: float, the width of the rectangle
    :return: float, the area of the rectangle
    """
    return length * width

# Example usage
rectangle_length = 5.0
rectangle_width = 3.0

# Calculate the area
area = calculate_area(rectangle_length, rectangle_width)

# Output the result
print(f"The area of the rectangle with length {rectangle_length} and width {rectangle_width} is {area} square units.")
