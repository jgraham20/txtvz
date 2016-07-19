# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

import nltk
from nltk.tokenize import WordPunctTokenizer

text = "Test"

class segment:

    tree = None

    def __init__(self, t):
        self.tree = t

    def osis(self):
        print ("OSIS")
        for subtree in self.tree.subtrees(filter=lambda t: t.label() == 'BCV'):
            print(subtree.label())
            print(subtree.leaves())


class BCVParser:
    tree = None
    postoks = None
    toks = None

    def __init__(self):
        patterns = [
            (r'G(?:e(?:n(?:esis)?)?|n)$', 'GN'),  # Genesis
            (r'Ex(?:o(?:d(?:us)?)?)$', 'EX'),  # Exodus
            (r'J(?:n|ohn|hn)$', 'JN'),  # John
            (r'(?:I J(?:n|hn|o(?:hn?)?)|1(?:J(?:n|ohn|hn)|J(?:n|hn|o(?:hn?)?)|st John)|First John)$', '1JN'),
            # 1st John
            (r'[:]$', 'COL'),  # Colon
            (r'[\.]$', 'DOT'),  # Period
            (r'[-]$', 'THRU'),  # Through TODO:Add more through logic
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
            (r'.*', 'XX')  # nouns (default)
        ]

        grammar = r"""
            BBOOK:
                {<GN>}  # Genesis
                {<EX>}  # Exodus
                {<1JN>} # First John
                {<JHN>} # John

            BCV:
                {<BBOOK><CD><COL><CD>} # Book followed by chap and verse
        """

        self.regexp_tagger = nltk.RegexpTagger(patterns)
        self.chunker = nltk.RegexpParser(grammar)

    def leaves(self, label):
        """Finds tagged nodes of a chunk tree."""
        for subtree in self.tree.subtrees(filter=lambda t: t.label() == label):
            yield subtree.leaves()

    def parse(self, text):
        self.toks = WordPunctTokenizer().tokenize(text)
        self.postoks = self.regexp_tagger.tag(self.toks)
        t = self.chunker.parse(self.postoks)
        tree = segment(t)

        return tree

if __name__ == '__main__':
    p = BCVParser()
    seg = p.parse('Genesis 1:1')
    print(seg.osis())