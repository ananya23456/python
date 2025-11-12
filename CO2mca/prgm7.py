word=input("Enter a word:")
if len(word)>=3:
    if word.endswith("ing"):
        word+="ly"
    else:
         word+="ing"
else:
    print("Word is too short to modify.")
print("Modified word:",word)    
