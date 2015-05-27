#!/usr/bin/env python3
'''
Tokenizes the input file
Usage: ./tokenizer.py infile > tokenized_file

Input file: one sentence per line
Output file: like input, but tokenized and stemmed with stopwords removed

List of stopwords from: https://code.google.com/p/stop-words/
Note had to change name of script because of problems with NLTK

29 May 2015 (based on code from exercise 1)
Anna Currey, Alina Karakanta, Kata Naszadi
'''

import argparse, string, sys
from nltk.stem.snowball import EnglishStemmer
__version__ = '1.1'     # includes stopword removal and stemming

# variables needed
LINEBREAK = '\n'
WORD_SEP = ' '

# keep letters, digits, whitespace
KEEP_CHARS = string.ascii_letters + string.digits + string.whitespace
# also keep apostrophe and dash (as discussed in class)
KEEP_CHARS += '\'' + '-'

# stopwords file and set
stopwords_file = 'stop-words.txt'


# main function
def main():
    # parse command-line arguments
    parser = get_parser()
    args = vars(parser.parse_args())
    infile_name = args['infile']
    
    # get stopwords
    stopwords = get_stopwords(stopwords_file)
    
    # apply to each line in the input
    with open(infile_name, 'r') as infile:
        for line in infile:
            # change to lowercase
            line = line.lower()
            
            # remove punctuation / special chars
            line = remove_punct(line, False)
            
            # trim spaces
            line = remove_spaces(line)
            
            # remove stopwords and stem other words
            line = stopwords_stem(line, stopwords)
            
            # now write to output
            sys.stdout.write(line + LINEBREAK)

#tokenize a line
def tokenize(line):
    # get stopwords
    stopwords = get_stopwords(stopwords_file)

    # change to lowercase
    line = line.lower()

     # remove punctuation / special chars
    line = remove_punct(line, False)

    # trim spaces
    line = remove_spaces(line)

    # remove stopwords and stem other words
    line = stopwords_stem(line, stopwords)

    return line


# command-line argument parser
def get_parser():
    parser = argparse.ArgumentParser()
    
    # infile name (required argument)
    parser.add_argument('infile', help='file to be tokenized', 
                        metavar='infile', type=str)
    
    # version info (optional)
    parser.add_argument('-v', '--version', help='displays current version', 
                        action='version', version='%(prog)s '+__version__)
    
    return parser


# reads in stopwords file and stores words in a set
# takes the stopwords filename; returns the set of stopwords
def get_stopwords(filename):
    # set containing stopwords
    stopwords = set()
    with open(filename, 'r') as stop_file:
        # one word per line
        for line in stop_file:
            word = line.strip()
            # ignore blank lines and spaces
            if word != '':
                stopwords.update(word)
    return stopwords

# removes punctuation and special characters from a string
# anything that is not a letter or a digit is replaced by a space
def remove_punct(inline, add_space):
    outline = ''
    for letter in inline:
        # if it is a letter or a digit or a space
        if letter in KEEP_CHARS:
            # keep it
            outline += letter
        else:
            if add_space:
                # replace with a space
                outline += ' '
            else:
                # do nothing
                pass
    return outline


# removes starting and trailing spaces and reduces multiple spaces to one
# should be run after remove_punct since that can introduce extra spaces
def remove_spaces(inline):
    # remove trailing and leading spaces
    inline = inline.strip()
    
    # cases of multiple whitespace become single
    inline = ' '.join(inline.split())
    
    return inline


# removes stopwords and stem the word
# should be done after remove_punct since stopwords only have ' and - as punct
def stopwords_stem(inline, stopwords):
    # consider each word individually
    words = inline.split(WORD_SEP)
    out_words = []
    for word in words:
        # ignore stopwords
        if word not in stopwords:
            # stem word
            out_words.append(EnglishStemmer().stem(word))
    # convert back to line
    outline = WORD_SEP.join(out_words)
    return outline
    

if __name__ == '__main__':
    main()