# 23a Zipf's Law
import matplotlib.pyplot as plt
import nltk
from math import log
from __future__ import division

def zipf(text):
    # remove punctuation, uppercase letters
    urtext = [w.lower() for w in text if w.isalpha()]
    print 'Done removing punctuation and lowering case.'
    fdist = FreqDist(urtext)
    print 'Done running FreqDist'
    
    # words is a list of most common words descending
    words  = [fdist.most_common()[k][0] for k in range(len(fdist))]
    # wrank is a list of the occurences of words
    nwords = [fdist.most_common()[k][1] for k in range(len(fdist))]
    plt.plot(nwords)
    plt.xticks(range(len(words)), words)
    plt.xscale('log')
    plt.yscale('log')
    plt.show() 

# http://stackoverflow.com/questions/6974847/plot-with-non-numerical-data-on-x-axis-for-ex-dates
