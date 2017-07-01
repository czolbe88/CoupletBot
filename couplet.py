from rhyme import *
from nltk.corpus import stopwords
import itertools as it
import re
#couplet generator

stopwords = stopwords.words('english')

sent = "I'm in the base gym at noon on August 7, lifting a few hundred pounds over my chest, working off the days, waiting for the lays chips"

def couplet(sent):

    tokenized = tokenize(sent) # word tokenize and remove all punctuation
    filtered = list(filter(lambda x: x not in stopwords, tokenized)) #filter out stopwords
    #print(tokenized)

    #test every word for rhyme against each other

    bigrams = list(it.combinations(filtered,2)) #deal with condition where the 'rhyme' is actually the same word
    option = False #option True to enable pseudorhyme and false to disable
    for (x,y) in bigrams:

        tokenized_ = tokenized[:] #deal with the condition where there are is than one rhyme match in the sentence

        try:
            if (x == y and option == True):

                print("pseudorhyme: ", x)
                linebreak_positionx = tokenized_.index(x) + 1
                #print(linebreak_positionx)
                tokenized_.insert(linebreak_positionx, '\n')
                linebreak_positiony = tokenized_.index(x, linebreak_positionx + 1) +1
                #print(linebreak_positiony)
                tokenized_.insert(linebreak_positiony, '\n')

                detokenize = " ".join(tokenized_) #turn the tokenized sentence back into a string
                print(detokenize)
                return(detokenize)


            elif comparewords(x,y) == True and x != y :

                print("couplet rhyme: ", (x,y) )
                linebreak_positionx = tokenized_.index(x) + 1
                #print(linebreak_positionx)
                tokenized_.insert(linebreak_positionx, '\n')
                linebreak_positiony = tokenized_.index(y) +1
                #print(linebreak_positiony)
                tokenized_.insert(linebreak_positiony, '\n')

                detokenize = " ".join(tokenized_) #turn the tokenized sentence back into a string
                print(detokenize)
                return(detokenize)

        except:
            pass


####


passage = """What likely happened was that the agenda from the very beginning was to maximize the exposure of the "generous" goodwill
 gesture for NS50 publicity. Some top mind then suggested free rides for men in uniforms, because the  elites assume tha
t peasants are so kiam siap that they would be willing to don No.4 to save on bus fare. And certainly there will be a fe
w siao on who are thirsty for a photo op."""

def coupletize(passage):
    tokenized = sent_tokenize(passage)
    for sent in tokenized:
        return(couplet(sent))
