#alternative couplet finding mechanism
from rhyme import *
from nltk.corpus import stopwords
import itertools as it


stopwords = stopwords.words('english')

sent = "I am a chicken dog. I like a hog. I sleep like a log. I live in a bog."


def couplet(sent):
    tokenizedPassage = sent_tokenize(sent)  # break passage into a list of sentences
    numSentences = len(tokenizedPassage)
    verses = []

    for i in range(len(tokenizedPassage)):

        try:

            lw1 = tokenize(tokenizedPassage[i])[-1]


            if i < len(tokenizedPassage):
                lw2 = tokenize(tokenizedPassage[i+1])[-1]

            if lw1 != lw2:

                if comparewords2(lw1, lw2) == True :
                    verseForm = tokenizedPassage[i] + "\n" + tokenizedPassage[i + 1]
                    verses.append(verseForm)



        except:
            pass

    return verses


