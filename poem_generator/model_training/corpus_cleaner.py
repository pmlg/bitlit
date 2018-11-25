import string
import re


corpus = open('poe.txt')
new_corpus = open('poe_cleaned.txt', 'w')
rhymes = open('rhymes_poe.txt', 'w')
c = 1
corpus.readline()

blank_count = 3
for line in corpus.readlines():
    line = line.lstrip()
    line = line.rstrip(string.punctuation + string.whitespace)
    re.sub('[^a-z\n]', ' ', line)
    if line == '':
        blank_count += 1
        if blank_count < 2:
            print(line.lower())
            new_corpus.write(line.lower() + '\n')
    else:
        if blank_count <= 2:
            istitle = line[-1] in string.ascii_uppercase
            isauthor = line[0] in string.punctuation 
            if len(line) >= 5 and not istitle and not isauthor:
                l = re.sub('[^a-z\n]', ' ', line.lower())
                last_word = l.split()[-1]
                print(last_word)
                last_word = re.sub('[^a-z\n]', ' ', last_word.lower()) 
                last_word = last_word.split()[-1]
                rhymes.write(last_word + '\n')
                new_corpus.write(l + '\n')
        blank_count = 0
    c += 1

corpus.close()
new_corpus.close()
rhymes.close()
