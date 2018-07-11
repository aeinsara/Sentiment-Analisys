# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *
from collections import Counter
import math
from random import *

firstWord = ['خنده','عشق','شاد','خوب']
secondWord = ['گریه','تنفر','ناراحت','بد']

phrases = []
polarity = []
avg_phrase_pol = []
tweets = []

textDay = []
dayFile = open('day2.txt','r')
lines = dayFile.readlines()

for line in lines:
    tweets.append(line)
    for word in line.split():
        textDay.append(line)

print(textDay)

tagger = POSTagger(model='resources/postagger.model')

for j, tweet in zip(range(1,2700), tweets):
    #rand = randint(1, len(tweets)-1)
    tagged = tagger.tag(word_tokenize(tweet))

    for word in tagged:
        if word[1] == 'N':
            i = tagged.index(word)
            if i + 1 != len(tagged) :
                #print(i, word)
                if tagged[i+1][1] == 'N':
                    ph = word[0]+" "+ tagged[i+1][0]
                    if ph not in phrases:
                        phrases.append(ph)

                if tagged[i + 1][1] == 'AJ':
                    ph = word[0] + " " + tagged[i + 1][0]
                    if ph not in phrases:
                        phrases.append(ph)


tokens = str(textDay).split()

print()

for first_Word, second_Word, i in zip(firstWord, secondWord, range(0,len(firstWord))) :

    countPos = tokens.count(first_Word)
    countNeg = tokens.count(second_Word)
    print(textDay)
    print("countPos: ", countPos, first_Word,'\ncountNeg : ', countNeg, second_Word)

    for l in phrases:
        count = 0
        hitNearPos = 0
        hitNearNeg = 0

        first = word_tokenize(l)[0]
        second = word_tokenize(l)[1]
        
        for tweet in tweets:
            sent_tokens = word_tokenize(tweet)

            if first in sent_tokens :
                j = sent_tokens.index(first)
            if (j + 1) < len(sent_tokens):
                if sent_tokens[j + 1] == second:
                    if first_Word in sent_tokens:
                        hitNearPos += 1

                    if second_Word in sent_tokens:
                        hitNearNeg += 1

        if countNeg != 0 and hitNearPos != 0 and countPos != 0 and hitNearNeg != 0:
            polarity.append(math.log(float(countNeg * hitNearPos) / (countPos * hitNearNeg)))



    if len(polarity) != 0:
        avg_phrase_pol.append(sum(polarity)/ float(len(polarity)))
        print ("polarity ", first_Word , second_Word, ":\t" , sum(polarity)/ float(len(polarity)))

if len(avg_phrase_pol) != 0:
    avgDay = sum(avg_phrase_pol)/ float(len(avg_phrase_pol))
    print ('polarity avg :', avgDay)

'''
#............................................................................................................

phrases = []
polarity = []
avg_phrase_pol = []
tweets = []
textNight = []

nightFile = open('night2.txt','r')
lines = nightFile.readlines()

for line in lines:
    tweets.append(line)
    for word in line.split():
        textNight.append(line)

print(textNight)

#normalizer = Normalizer()
#normalizer.normalize(textNight)

#stemmer = Stemmer()
#stemmer.stem(textNight)

#lemmatizer = Lemmatizer()
#lemmatizer.lemmatize(textNight)
    
tokens = word_tokenize(textNight)

tagger = POSTagger(model='resources/postagger.model') 

for j in range(1, 500):
    rand = random.randint(1, len(tweets))
    tagged = tagger.tag(word_tokenize(tweets[rand]))

    for word in tagged:
        if word[1] == 'N':
            i = tagged.index(word)
            if i + 1 != len(tagged):
                if tagged[i+1][1] == 'N':
                    ph = word[0]+" "+ tagged[i+1][0]
                    if ph not in phrases:
                        phrases.append(ph)

                if tagged[i + 1][1] == 'AJ':
                    ph = word[0] + " " + tagged[i + 1][0]
                    if ph not in phrases:
                        phrases.append(ph)

tokens= str(textNight).split()

for first_Word, second_Word, i in zip(firstWord, secondWord, range(0, len(firstWord))):

    countPos = tokens.count(first_Word)
    countNeg = tokens.count(second_Word)

    for l in phrases:
        count = 0
        hitNearPos = 0
        hitNearNeg = 0

        first = word_tokenize(l)[0]
        second = word_tokenize(l)[1]

        for tweet in tweets:
            sent_tokens = word_tokenize(tweet)

            print(sent_tokens)

            if first in sent_tokens :
                j = sent_tokens.index(first)
            if (j + 1) < len(sent_tokens):
                if sent_tokens[j + 1] == second:
                    if first_Word in sent_tokens:
                        hitNearPos += 1

                    if second_Word in sent_tokens:
                        hitNearNeg += 1


        if countPos != 0 and hitNearPos != 0 and countNeg != 0 and hitNearNeg != 0:
            polarity.append(math.log(float(countNeg * hitNearPos) / (countPos * hitNearNeg)))

    if len(polarity) != 0:
        avg_phrase_pol.append(sum(polarity) / float(len(polarity)))
        print('avg_phrase_pol[i]', avg_phrase_pol[i])

if len(avg_phrase_pol) != 0:
    avgNight= sum(avg_phrase_pol) / float(len(avg_phrase_pol))
    print('avg', avgNight)
'''