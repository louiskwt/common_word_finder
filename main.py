import collections
import pandas as pd

# Read input file
file = open('sample.txt', encoding="utf8")
a = file.read()

# stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['mr', 'mrs', 'one', 'two', 'said']))

# Instantiate a dictionary, and for every word in the file,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}

for word in a.lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("â€œ", "")
    word = word.replace("â€˜", "")
    word = word.replace("*", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print the most common words
n_print = int(input("How many most common words to print: "))
print("\n The {} most common words are as follows: \n".format(n_print))

word_counter = collections.Counter(wordcount)

with open('wordlist.txt', mode='w') as text:
    text.write("Most common words: ")
    text.write("\n")
    for word, count in word_counter.most_common(n_print):
        print(word, ': ', count)
        text.write(word + " : " + str(count))
        text.write("\n")
    text.close()

print('Finished! The Wrod List is ready!')
file.close()
