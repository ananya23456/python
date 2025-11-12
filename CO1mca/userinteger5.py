numbers=list(map(int,input("Enter integers separated by space:").split()))
result=['over' if n>100 else n for n in numbers]
print("Modified list;",result)
