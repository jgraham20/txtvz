# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

import nltk
from nltk.tokenize import WordPunctTokenizer
text = "Test"

class BCVParser:

    def __init__(self, grammar):

        patterns = [
             (r'G(?:e(?:n(?:esis)?)?|n)$', 'GN'),   # Genesis
             (r'Ex(?:o(?:d(?:us)?)?)$', 'EX'),      # Exodus
             (r'J(?:n|ohn|hn)$', 'JN'),             # John
             (r'(?:I J(?:n|hn|o(?:hn?)?)|1(?:J(?:n|ohn|hn)|J(?:n|hn|o(?:hn?)?)|st John)|First John)$', '1JN'), #1st John
             (r'[:]$', 'COL'),                       # Colon
             (r'[\.]$', 'DOT'),                      # Period
             (r'[-]$', 'THRU'),                      #Through TODO:Add more through logic
             (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),        # cardinal numbers
             (r'.*', 'XX')                           # nouns (default)
         ]

        grammar = r"""
            BBOOK:
                {<GN>}  # Nouns and Adjectives, terminated with Nouns
                {<EX>}  # Nouns and Adjectives, terminated with Nouns
                {<1JN>}
                {<JHN>}  # Nouns and Adjectives, terminated with Nouns

            BCV:
                {<BBOOK><CD><COL><CD>}
        """

        self.regexp_tagger = nltk.RegexpTagger(self.patterns)
        self.chunker = nltk.RegexpParser(grammar)

    def parse(self, text):

        toks = WordPunctTokenizer().tokenize(text)
        postoks = self.regexp_tagger.tag(toks)

        print (toks)
        print (postoks)

    #final = [stemmer.stem(tagged_word[0]) for tagged_word in postoks]

    # def getTree(self):
    #     tree = self.chunker.parse(postoks)
    #     print (tree)