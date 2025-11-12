text=input("enter a line of text:")
words=text.lower().split()
word_count={}
for word in words:
    word=word.lower()
    word_count[word]=word_count.get(word,0)+1
    print("\nword occurrence:")
    for word,count in word_count.items():
        print(f"{word}:{count}")
