# -*- coding: utf-8 -*-

import tweepy
import csv
import time
import re
'''
consumer_key = "WEkpOOdWGmjmwKI4MInAAyS2j"
consumer_secret = "dh6ot84dDvbNzwCopu3LWcmqm9OWgu4Ef3mb3QDV2Jk5xFHC7o"
access_token = "1014847891117150208-pEkQcavuF0a2iYYn927h51Rb2gNDgP"
access_token_secret = "L0AhKU4P2uha9AURKf7U1viFXu6O4DfGa11hwLiD8pFz3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

dayFile = open('day.txt', 'a', encoding="utf-8")
dayFile.close()

nightFile = open('night.txt', 'a', encoding="utf-8")
nightFile.close()


i = 0
for tweet in tweepy.Cursor(api.search, q="#انقلاب", lang="fa", tweet_mode='extended').items():

    ts = time.strftime('%H', time.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))

    if 1 < int(ts) < 5:  # check it is night tweet
        nightFile = open('night.txt', 'a', encoding="utf-8")
        nightWriter = csv.writer(nightFile)

        nightText = tweet._json['full_text']
        # ...............................* normalize night text *...............................
        nightText = re.sub( r'[a-zA-Z]', '', nightText)
        nightText = re.sub(r'[/.,:"@?]', '', nightText)
        nightText = re.sub(r'[0-9]', '', nightText)
        nightText = re.sub(r'[\n\n]', ',', nightText)
        nightText = re.sub(r'[\n]', ' ', nightText)
        nightText = re.sub(r'[,]', '\n', nightText)

        nightWriter.writerow([nightText])
        nightFile.close()
    elif 7 < int(ts) < 11:  # check it is day tweet
        dayFile = open('day.txt', 'a', encoding="utf-8")
        dayWriter = csv.writer(dayFile)

        dayText = tweet._json['full_text']
        # ...............................* normalize day text *...............................
        dayText = re.sub(r'[a-zA-Z]', '', dayText)
        dayText = re.sub(r'[/.:"@?]', '', dayText)
        dayText = re.sub(r'[0-9]', '', dayText)
        dayText = re.sub(r'[\n\n]', ',', dayText)
        dayText = re.sub(r'[\n]', ' ', dayText)
        dayText = re.sub(r'[,]', '\n', dayText)

        dayWriter.writerow([dayText])
        dayFile.close()

    print ("i === ",i , "\t", tweet._json['created_at'], tweet._json['full_text'])
    i = i + 1
	
'''
#.............................* clean data of dayText *...........................
ascciList = [1570, 1574, 1575, 1576, 1578 ,1579,1580,1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,
             1601, 1602, 1604, 1605, 1606, 1607, 1608, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1662,1670,
             1688, 1705, 1711, 1740]

dayFile1 = open('day.txt','r', encoding="utf-8")
lines = dayFile1.readlines()
dayFile1.close()

flag = False

dayFile = open('day2.txt', 'w', encoding="utf-8")

for line in lines:
    for ch in line:
        if ch == '"' :
            if flag == False :
                flag = True
            else:
                flag = False
                dayFile.write('\n')
        else :
            if (ord(ch) in ascciList) or ch == ' ' or ch == '\n':
                if ch == '\n':
                    ch = ' '
                dayFile.write(ch)
            else :
                dayFile.write(' ')

dayFile.close()

#.............................* clean data of nightText *...........................
dayFile1 = open('night.txt','r', encoding="utf-8")
lines = dayFile1.readlines()
dayFile1.close()

flag = False

dayFile = open('night2.txt', 'w', encoding="utf-8")

for line in lines:
    for ch in line:
        if ch == '"' :
            if flag == False :
                flag = True
            else:
                flag = False
                dayFile.write('\n')
        else :
            if (ord(ch) in ascciList) or ch == ' ' or ch == '\n':
                if ch == '\n':
                    ch = ' '
                dayFile.write(ch)
            else :
                dayFile.write(' ')

dayFile.close()


