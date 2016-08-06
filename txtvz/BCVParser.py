# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

import nltk
from nltk.tokenize import WordPunctTokenizer, RegexpTokenizer

text = "Test"

class segment:

    tree = None
    #nltk.tree.Tree.
    def __init__(self, t):
        self.tree = t

class BCVParser:
    tree = None
    postoks = None
    toks = None

    def __init__(self):
        patterns = [
            (r'(i)|(1st)|(first)', '1'),
            (r'(?:ii?|2nd|second)', 'TWO'),
            (r'(?:iii?)|3rd|third', 'THREE'),
            (r'g(?:e(?:n(?:i(?:[ei]s(?:[eiu]s)|s[eiu]s)|n(?:i(?:[ei]s(?:[eiu]s)|s[eiu]s)|e(?:es[eiu]s|s[eiu]s|is(?:[eiu]s)?)|sis)|e(?:es[eiu]s|is(?:[eiu]s)?|s(?:us|[ei]s?))|sis)?)?|n)', 'GN'),  # Genesis
            (r'ex(?:o(?:d(?:us)?)?)', 'EX'),  # Exodus
            (r'm(?:ark|k|rk)', 'MK'),
            (r's(?:olomon)', 'SOL'),
            (r'j(?:n|ohn|hn)', 'JN'),  # John
            (r'titus', 'TITUS'),
            (r'w(?:isdom)', 'WIS'),
            (r'(chapter)', 'CH'), #TODO:Add forms ch chap
            (r'(verse)', 'CH'), #TODO:Add forms vv
            (r'[:]$', '.'),  # Colon
            (r'[\.]$', '.'),  # Period
            (r'(through)|(thru)|(-)', 'THRU'),  # Through TODO:Add more logic
            (r'to', 'TO'),
            (r'in', 'IN'),
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
            (r'\s', 'WS')
        ]

        grammar = r"""

            CV:
                {<CD><.><CD><THRU>*<CD>*}
                {<CD><DOT><CD><THRU>*<CD>*}
                {<CD><THRU><CD>}
            B:
                {<GN>}  # Genesis
                {<EX>}  # Exodus
                {<TITUS>}  # Titus
                {<WIS><NN>*<SOL>}
                {<1>*<NN>*<JN>}
                {<TWO>*<NN>*<JN>}
                {<THREE>*<NN>*<JN>}# John or Epistle of John
                {<MK>}
            BCV:
                {<B><CV>} # Book followed by chap and verse
        """
        self.default_tagger = nltk.DefaultTagger('NN')
        self.regexp_tagger = nltk.RegexpTagger(patterns, backoff=self.default_tagger)
        self.chunker = nltk.RegexpParser(grammar)
        self.tokenizer = RegexpTokenizer('(?:1ST|2ND|3RD)|(?:\d+|[a-zA-Z]+|[=:\'\.()-])|\s+')

    def parseCV(self, node):
        cv = '.'
        for l in node.leaves():
            if l[1] == '.':
                cv = cv + '.'
            elif l[1] == 'THRU':
                cv = cv + '-'
            else:
                cv = cv + l[0]
        return cv

    def parseBook(self, node):
        return ''.join(map(lambda x: x[1], node.leaves()))


    def osis(self, node):
        osis = ''

        for n in node:
            print (n)
            if isinstance(n, nltk.tree.Tree):
                if n.label() == 'B':
                    osis = osis + self.parseBook(n)
                elif n.label() == 'CV':
                    osis = osis + self.parseCV(n)
                else:
                    return self.osis(n)
        return osis

    def parse(self, text):
        self.toks = [x.lower() for x in self.tokenizer.tokenize(text) if x.strip() != '']
        self.postoks = self.regexp_tagger.tag(self.toks)
        t = self.chunker.parse(self.postoks)

        return t

if __name__ == '__main__':

    p = BCVParser()
    seg = p.parse('First John 1:1')
    print(p.osis(seg))
    # seg = p.parse('John 1:5')
    # print(seg.printseg())
    # seg = p.parse('2ND John 1:1')
    # print(seg.printseg())
    seg = p.parse('2ND John 1:1-2')
    print(p.osis(seg))
    #seg = p.parse('The Wisdom Solomon 1:1')
    # print(seg.printseg())
    seg = p.parse('Mark1through2')
    print(p.osis(seg))
    seg = p.parse('Titus 1:1 thru 2')
    print(p.osis(seg))
    # seg = p.parse('Exod 1:1 cf 3')
    # print(seg.printseg())
