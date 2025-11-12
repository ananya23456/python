string=input("Enter a string:")
n=int(input("Enter the index of the character to remove:"))
if n<0 or n>= len(string):
    print("Invalid index!")
else:
    new_string=string[:n]+string[n+1:]
    print("string after removing character:",new_string)
