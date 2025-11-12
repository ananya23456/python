color_list1=input("Enter first list of colors (comma-separated):").split(",")
color_list2=input("Enter second list of colors (comma-separated):").split(",")
color_list1=[color.strip() for color in color_list1]
color_list2=[color.strip() for color in color_list2]
unique_colors=[color for color in color_list1 if color not in color_list2]
print("colors in list1 not in list2:",unique_colors)
