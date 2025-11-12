filename=input("Enter a file name(with extension):")
parts=filename.split('.')
if len(parts)>1:
    print("File extension  is:",parts[-1])
else:
    print("No extension found in the file name.")
