
# ----------------- # NEW Python Project IDEA # ----------------- #
# NEXT STEP: use mongodb to collect semantic analysis of certain websites RSS feeds

import feedparser
import matplotlib.pyplot as plt

mydict = {}

ignored_words = ['','the','a','to','of','in','and','for','on','was',\
    'with','that','his','are','as','from','man','an','over','according',\
    'after','is','has','her','into','by','said','he','here','who','illinois','been','have','at','new',\
    'but','wednesday','thursday','be','says','some','this','back','they','will','when',\
    'chicago', 'about', 'it', 'their', 'what', 'more', 'people','how','could','many','during','west','side','year','heres','found']

NewsFeed = feedparser.parse("https://www.chicagotribune.com/arcio/rss/category/news/breaking/?query=display_date:%5Bnow-2d+TO+now%5D+AND+revision.published:true&sort=display_date:desc#nt=instory-link")
NewsFeed2 = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

#-----Helper-Functions-----#
def remove_punctuation(foo):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for x in foo:
        if x in alphabet:
            out += x
    return out
#--------------------------#

# collect words from RSS feed(s)
RSS_feeds = ["https://www.chicagotribune.com/arcio/rss/category/news/breaking/?query=display_date:%5Bnow-2d+TO+now%5D+AND+revision.published:true&sort=display_date:desc#nt=instory-link",\
    "http://feeds.bbci.co.uk/news/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml","https://www.aljazeera.com/xml/rss/all.xml","https://feeds.npr.org/1001/rss.xml"]
for feed in RSS_feeds:
    NewsFeed = feedparser.parse(feed)
    for entry in NewsFeed.entries:
        temp = entry.summary.split()
        for word in temp:
            word = remove_punctuation(word.lower())
            if word not in ignored_words:
                if word not in mydict:
                    mydict.update({word:1})
                else:
                    mydict[word] += 1

# remove uncommon entries
temp = mydict.copy()
for x in temp:
    if temp[x] <= 3:
        mydict.pop(x)

# retrieve the top ten words and total number of words
mysum = sum(mydict.values())
topten = {}
count = 0
miter = 0
while count < 10 and miter < 100000:
    miter += 1
    maxi = max(mydict.values())
    for x in mydict:
        if mydict[x] == maxi:
            topten.update({x:mydict[x]})
            try:
                mydict.pop(x)
            except:
                print("break here!")
            count += 1
            break

# display word counts in a pie chart:
#**first we add an "other" category
#topten.update({"other":mysum-sum(topten.values())})
fig1, ax1 = plt.subplots()
ax1.pie(topten.values(), labels=topten.keys(), autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

print(topten)
print(mysum)

# for entry in NewsFeed2.entries:
#     if word in entry.summary:
#         print (entry.published)
#         print ("***BBC***")
#         print (entry.summary)
#         print ("***BBC***") 