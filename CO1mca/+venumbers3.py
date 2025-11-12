numbers=[-5,3,-2,9,0,-8,7]
positive_numbers=[num for num in numbers if num>0]
print("a)positive numbers:",
      positive_numbers)


n=int(input("\nEnter how many numbers you want to square:"))
nums=[int(input(f"enter number{i+1}:"))for i in range(n)]
squares=[x**2 for x in nums]
print("b)squares of numbers:",squares)


word=input("\nEnter a word:")
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print("c)vowels in the word:",vowels)

word2=input("\nEnter another word:")
ordinal_values=[ord(ch)for ch in word2]
print("d)ordinal values:",
      ordinal_values)
