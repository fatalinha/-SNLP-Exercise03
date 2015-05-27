"""
Usage: python ./ex03.py

Anna Currey, 2554284
Alina Karakanta, 2556612
Kata Naszadi, 2556762
"""
from __future__ import division
import tokenizer
from sets import Set


dataPath="data/"
words=["bass", "crane", "motion", "palm", "plant", "tank"]

def read_data(word, type):
    """returns list of tuple(meaning, set(words))"""
    res =[]
    file=open(dataPath+word+"."+type, "r")
    while True:
        line=file.readline()
        if line=="":
            break
            #new def
        if line[0]=="#":
            line=line.split()
            #meaning is  word%meaning
            meaning=line[1]
            #definition
            line=file.readline()
            line=tokenizer.tokenize(line)
            words=line.split()
            res.append((meaning,set(words)))
    return res

def overlap(D, T):
    res = 2 * len(D.intersection(T)) / (len(D)+len(T))
    return res






if __name__=="__main__":
    pass

