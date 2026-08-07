def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width 
    print(f"Rectangle with length {length} and width {width}") # print what number did we put it
    print(f"Area = {length} × {width} = {area}") # what the nuber of area use to calculate and show result
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_trangle_area(height, base):
    """Calculates and displays trangle area"""
    area = 0.5 * height * base
    print(f"Trangle with height {height} and base {base}") # print what number did we put it
    print(f"Area =  0.5 × {height} × {base} = {area}") # what the number of area use to calculate and show result
    print()

print("Calculating triangle areas:")
calculate_trangle_area(5, 3)
calculate_trangle_area(10, 7)