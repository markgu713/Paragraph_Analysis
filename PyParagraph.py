import os
import csv
import re

textpath = os.path.join("..","Paragraph_Analysis", "paragraph.txt")

with open (textpath, encoding='utf-8') as textFile: 
    text = textFile.read()
    # split the paragraph into individual words
    word = text.split()
    # sentence count
    sentence = re.split("(?<=[.!?]) +", text)
    # calculate approximate letter count (per word)
    letterInWord = [len(letter) for letter in word] 
    avgLetterCount = round(sum(letterInWord) / len(word), 1)
    # calculate average sentence length
    wordsInSentence = [len(sen.split()) for sen in sentence]  
    avgSenLen = round(sum(wordsInSentence) / len(sentence), 1)

print("Paragraph Analysis")
print("------------------")
print(f"Approximate Word Count: {len(word)}")
print(f"Approximate Sentence Count: {len(sentence)}")
print(f"Average Letter Count: {avgLetterCount}")
print(f"Average Sentence Length: {avgSenLen}")
