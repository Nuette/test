from __future__ import division
from collections import defaultdict
import re

# calculate the number of times there was a switch between languages
# count the number of languages in text
# count the number of words per language
# count the number of words in text
# calculate the M-index
# calculate the I-index
regex = r"\w_(\w\w\w?)$"
languages = defaultdict(int) #unique language as key and amount of words per language as value
nuofswitched = 0 #number of times a switch occured in the text
with open("lid_tagged_corpus.txt") as f:
    corpus = f.readlines()
    prev_lang = 'en'
    for line in corpus:
        list_tagged = []
        word_list = line.split(' ')
        for w in word_list:
            matches = re.search(regex, w)
            if matches:
                language_name = matches.group(1)
                languages[language_name] += 1
                if language_name != prev_lang:
                    nuofswitched += 1
                prev_lang = language_name

numof_lang = len(languages)  # total number of words in a language

#calculate the number of words in the corpus
numof_words = 0
for m in languages:
    numof_words = numof_words + languages[m]

#calculate the M-index
sum_p = 0
for m in languages:
    j = languages[m] #total number of words in a language m
    p = j/numof_words
    expo_p = p ** 2
    sum_p = sum_p + expo_p

MIndex = (1 - sum_p) / (numof_lang-1) * sum_p

#calculate the I-index
n = 1/(numof_lang-1)
Iindex= n * nuofswitched

