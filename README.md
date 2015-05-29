# -SNLP-Exercise03
Word Sense Disambiguation

## Statistical Natural Language Processing
Summer Semester 2015
29 May 2015

## Group members
Anna Currey, 2554284, amscurrey@gmail.com

Alina Karakanta, 2556612, alinak@coli.uni-saarland.de

Kata Naszadi, 2556762, b.naszadi@gmail.com

## Scripts
tokenizer.py

Tokenizes the input file
Usage: ./tokenizer.py infile > tokenized_file

Input file: one sentence per line
Output file: like input, but tokenized and stemmed with stopwords removed

List of stopwords from: https://code.google.com/p/stop-words/

ex03.py

Word Sense Disambiguation implementation
Computes Dice coefficient, classifies documents according to the score and prints the number of misclassifications.
