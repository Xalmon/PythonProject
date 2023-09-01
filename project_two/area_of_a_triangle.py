def check_area_of_triangle(base, height):
    area = 0.5 * int(base) * int(height)
    return area


base_value = input("Enter the base of the triangle: ")
height_value = input("Enter the height of the triangle: ")
area_result = check_area_of_triangle(base_value, height_value)
print("The area of the triangle is:", area_result)
