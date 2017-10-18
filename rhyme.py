from nltk.corpus import wordnet as wn
from nltk import *
from nltk.corpus import cmudict
from nltk.tokenize import RegexpTokenizer
from random import randint
from pronouncing import *
import re

testsent1 = " what is for dinner? "  # key in test sentence
testsent2 = "I hope it is good food"

dicto = cmudict.dict()  # dictionary object containing wordname:pronunciation of all words in cmudict

tokenizer = RegexpTokenizer(r'(\w+\'+\w+|\w+)')


def tokenize(sentence):
    sentence = tokenizer.tokenize(sentence)
    return (sentence)


def last_word(sentence):  # obtains last word of sentence
    tokenize(sentence)  # tokenizes all \w+ occurences
    lw = sentence[-1]
    return (lw)


def last_word_pos(last_word):  # obtains the pos of a word
    last_wordpos = (pos_tag([last_word]))
    last_wordpos = last_wordpos[0][1]
    return (last_wordpos)


def syllables(last_word):  # function that obtains syllables of a word
    syllables = dicto[last_word]
    return (syllables)


def matchrhymes(syllables):  # function that returns a list of words (from cmudict) that rhyme
    pron = syllables[-1][-2:]
    rhymes = [word for word in dicto if dicto[word][-1][-2:] == pron]
    return (rhymes)


def comparewords(word1, word2):  # function that checks if two words are rhymes, added no 'ing' option
    pron1 = syllables(word1)
    pron2 = syllables(word2)
    if re.search('ing', word1 + word2) == None:
        if pron1[-1][-2:] == pron2[-1][-2:]: # note: syllables from cmudict.dict() are returned as a list within a list
            return (True)

        else:
            return (False)


def comparewords2(word1, word2):  # uses the pronouncing library
    if word2 in rhymes(word1):
        return (True)
    else:
        return (False)


def obtainrhyme(sentence1, sentence2):  # creates rhymes
    lastword = last_word(sentence1)
    syllable = syllables(lastword)
    rhymes_list = matchrhymes(syllable)  # list of rhyming words

    print(rhymes_list)

    lastword2 = last_word(sentence2)
    to_match = wn.synsets(lastword2)[0]

    rhymes_synsets = [wn.synsets(word) for word in
                      rhymes_list]  # now find the rhymign word most similar to last word in sentence2
    flattened = [synset for sublist in rhymes_synsets for synset in sublist]

    synset_scores = {}
    for synset in flattened:
        score = wn.wup_similarity(synset, to_match)
        synset_scores[synset] = score
    print("using wup_similarity")
    for i in synset_scores:
        print(i, synset_scores[i])

    most_similar = max(synset_scores)
    print(most_similar)
    print(synset_scores[most_similar])

    most_similarnames = most_similar.lemma_names()
    print(most_similarnames)


# for selecting a random rhyme
'''
    random_number = randint(0, len(rhymes_list) - 1)
    random_rhyme = rhymes_list[random_number]
    for rhyme in rhymes_list:
        print(rhyme)
    print(random_rhyme)
    return(random_rhyme)
'''


def rhymeword(word1):  # needs correction
    pron = dicto[word1]
    rhymes = [rhyme for rhyme in dicto if dicto[rhyme][-1][-2:] == pron[-1][-2:]]
    print(rhymes)
    return (rhymes)

##################################
