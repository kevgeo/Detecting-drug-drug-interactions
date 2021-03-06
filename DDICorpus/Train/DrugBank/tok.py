from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
import string

import re
import random
from os import path

with open("file.txt") as f1:
    text1 = f1.read()

filenames = re.split(r'[\n\r]+', text1)

for filename in filenames:
	tree = ET.parse(filename)
	root = tree.getroot()

	stop_words = set(stopwords.words("english"))  # load stopwords

	for sentence in root.findall('sentence'):
		text=sentence.get('text')
		#print (text)	
		example_words = word_tokenize(text)
		#print (example_words)
		# removing punctuations
		example_words_punc = list(filter(lambda x: x not in string.punctuation, example_words))
		#print (example_words_punc)
		# removing stopwords 
		cleaned_text = list(filter(lambda x: x not in stop_words, example_words_punc))
		print(cleaned_text)
		#append the list into a file line by line

