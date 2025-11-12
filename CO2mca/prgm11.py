area_square = lambda side: side ** 2
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height
print("Area of square (side=5):", area_square(5))
print("Area of rectangle (length=10, width=4):", area_rectangle(10, 4))
print("Area of triangle (base=8, height=6):", area_triangle(8, 6))
