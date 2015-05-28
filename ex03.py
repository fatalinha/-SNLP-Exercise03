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
            res.append((meaning,Set(words)))
    return res

def overlap(D, T):
    res = 2 * len(D.intersection(T)) / (len(D)+len(T))
    return res

def classify(test, definitions):
    best_sim=0
    cl=""
    print(test)
    for label, set in definitions:

        sim=overlap(set, test)

        print label, sim
        #update best
        if sim>best_sim:
            best_sim=sim
            cl=label
    return cl

if __name__=="__main__":
    #list holding tuple(misclassifications, allwords) in order of words
    misClassifications=[]
    for word in words:
        misclass=0
        numOfTest=0
        #list holding tuple(meaning, set(defiitions)
        definitions=read_data(word, 'definition')
        #list holding tuple(meaning, set(text)
        tests=read_data(word,'test')
        for label, set in tests:
            numOfTest+=1
            cl= classify(set,definitions)
            if cl != label:
                misclass+=1

        misClassifications.append((misclass,numOfTest))

    print(misClassifications)


