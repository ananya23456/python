list1 = list(map(int,input("Enter integers for first list(space separated):").split()))
list2 = list(map(int,input("Enter integers for second list(space separated):").split()))
same_length = len(list1) == len(list2)
print("Both lists have same length:", same_length)
same_sum = sum(list1) == sum(list2)
print("Both lists have the same sum:", same_sum)
common_values = set(list1)& set(list2)
if common_values:
    print("common values in both lists:", common_values)
else:
    print("No common values in both lists.")
