import pandas as pd

file = "C:\\Users\\jmank\\Desktop\\VisStudioRepos\\COS-470-570-Exercise4\\quotes.tsv"

df = pd.read_csv(file, sep= '\t')

column = 'Author'
name = "Alexandre Dumas"
count = (df[column] == name).sum()

print(f"{name} has {count} quotes in the file")

longest = ""
author = ""
count = 0
for i, row in df.iterrows():
    quote = row['Quote']
    current_author = row['Author']
    words = quote.split()
    length = len(words)
    if length > count:
        max = length
        longest = quote
        author = current_author

print(f"{author} has the longest line with {max} words.")

word = "one"
one_authors = set()
for i, row in df.iterrows():
    quote = row['Quote']
    author = row['Author']
    if word in quote: 
        one_authors.add(author)


quotes = " ".join(df['Quote'])
words = quotes.split()
count = {}

print(f"Authors who quotes use the word 'one': {one_authors}")

for word in words:
    count[word] = count.get(word, 0) + 1

sort = sorted(count.items(), key = lambda x: x[1], reverse = True)

num_results = 5

print(f"Ten most used words: ")
for word, count in sort[:num_results]:
    print(f"'{word}': {count} times")
print("\nTen least used words: ")
for word, count in sort[-num_results:]:
    print(f"'{word}': {count} times")