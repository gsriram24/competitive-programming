import re
with open('words.txt') as f:
    wordlist = [word for line in f for word in line.split()]
longest_word = ''

for word in wordlist:
    if(len(word) <= len(longest_word)):
        continue
    if(re.match('[gkmqvwxz]', word)):
        continue
    longest_word = word
print(longest_word)
