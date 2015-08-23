from cStringIO import StringIO
import fileinput, string, pickle, os
import nltk
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
import pandas as pd
import csv
from gensim import corpora, models

data = []

with open('DC.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		data.append(row)

data = np.array(data)

refined_data = []

symbols = [".", "[", "]", "{", "}", "1", "2", "3", "4","5", "6", "7", "8", "9", "0", "-", "#", "&", "(", ")", "/", ":", ",", ";", "m/s", "\\"]

for row in data[1:]:
    string = ""

    for entity in row :
        string = string + " " + entity.replace("\"","")

    for symbol in symbols:
        string = string.replace(symbol,"")

    refined_data.append(string.lower().split())

del data

stop_words = []

sw = file('sample.txt', 'r')
for word in sw:
    word = word.strip().strip('\n')
    if word not in stop_words:
        stop_words.append(word)
sw.close()

stop_words = set(stop_words)

i = 0
for row in refined_data:
    refined_data[i] = [ word for word in row if word not in stop_words ]
    i+=1

dictionary = corpora.Dictionary(refined_data)

corpus = [dictionary.doc2bow(text) for text in refined_data]

model = models.LdaModel(corpus, id2word=dictionary, alpha='auto', num_topics=10)


i = 0
for topic in model.print_topics(10):
    print "**********"
    print "topic:"  + str(i) + " "+ str(topic) 
    i+=1

topic_distri = []
for document in corpus:
    topic_distri.append(model.get_document_topics(document, minimum_probability=0))

for row in topic_distri:
    print row