# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import RegexpTokenizer
from txtvz.referencedb import ReferenceDB


class BCVParser:

    def __init__(self):

        self.referenceDB = ReferenceDB()

        patterns = [
            (r'(i)|(1st)|(first)', '1'),
            (r'(?:ii?|2nd|second)', 'TWO'),
            (r'(?:iii?)|3rd|third', 'THREE'),
            (r'g(?:e(?:n(?:i(?:[ei]s(?:[eiu]s)|s[eiu]s)|n(?:i(?:[ei]s' +
                '(?:[eiu]s)|s[eiu]s)|e(?:es[eiu]s|s[eiu]s|is(?:[eiu]s)?)' +
                '|sis)|e(?:es[eiu]s|is(?:[eiu]s)?|s(?:us|[ei]s?))|sis)?)?|n)',
                'GN'),  # Genesis
            (r'ex(?:o(?:d(?:us)?)?)', 'EX'),  # Exodus
            (r'm(?:ark|k|rk)', 'MK'),
            (r's(?:olomon)', 'SOL'),
            (r'j(?:n|ohn|hn)', 'JN'),  # John
            (r'titus', 'TITUS'),
            (r'w(?:isdom)', 'WIS'),
            (r'(chapter)', 'CH'),  # TODO:Add forms ch chap
            (r'(verse)', 'CH'),  # TODO:Add forms vv
            (r'[:]$', '.'),  # Colon
            (r'[\.]$', '.'),  # Period
            (r'(through)|(thru)|(-)', 'THRU'),  # TODO:Add more logic
            (r'to', 'TO'),
            (r'in', 'IN'),
            (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
            (r'\s', 'WS')
        ]

        grammar = r"""
            CONT:
                {<THRU><CD>}
                {<CH><CD>}
            CV:
                {<CD><.><CD><CONT>*}
                {<CD><DOT><CD><CONT>*}
                {<CD><CONT>}
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
                {<B><CV><CC>*} # Book followed by chap and verse
        """
        tokens = '(?:1ST|2ND|3RD)|(?:\d+|[a-zA-Z]+|[=:\'\.()-])|\s+'
        self.default_tagger = nltk.DefaultTagger('NN')
        self.regexp_tagger = nltk.RegexpTagger(patterns,
                                               backoff=self.default_tagger)
        self.chunker = nltk.RegexpParser(grammar)
        self.tokenizer = RegexpTokenizer(tokens)

    @staticmethod
    def parse_cv(node):
        for l in node.leaves():
            if l[1] == '.':
                yield '.'
            elif l[1] == 'THRU':
                yield '-'
            else:
                yield l[0]

    @staticmethod
    def parse_book(node):
        return ''.join(map(lambda x: x[1], node.leaves()))

    @staticmethod
    # @property??
    def iter_tree(tree):
        # print(repr(tree))
        for n in tree:
            # print(repr(n))
            if isinstance(n, nltk.tree.Tree):
                print(n.label())
                if n.label() == 'B':
                    yield BCVParser.parse_book(n)
                elif n.label() == 'CV':
                    yield from BCVParser.parse_cv(n)
                else:
                    yield from BCVParser.iter_tree(n)

    def parse(self, text):
        self.toks = [x.lower() for x in self.tokenizer.tokenize(text)
                     if x.strip() != '']
        self.postoks = self.regexp_tagger.tag(self.toks)
        t = self.chunker.parse(self.postoks)

        for a in BCVParser.iter_tree(tree=t):
            print(a)


if __name__ == '__main__':
    p = BCVParser()
    seg = p.parse('First John 1:1')
    # self.referenceDB.print()
    # print(p.osis(seg))
    # seg = p.parse('John 1:5')
    # print(seg.printseg())
    # seg = p.parse('2ND John 1:1')
    # print(seg.printseg())
    # seg = p.parse('John 1:1-2')
    # print(seg.osis())
    # seg = p.parse('Genesis 1:1-2')
    # print(seg.osis())
    # seg = p.parse('The Wisdom Solomon 1:1')
    # print(seg.printseg())
    # seg = p.parse('Mark1through2')
    # print(p.osis(seg))
    # seg = p.parse('Titus 1:1 thru 2')
    # print(p.osis(seg))
    # seg = p.parse('Exod 1:1 cf 3')
    # print(seg.printseg())
    # seg = p.parse('Titus 1:1-2 chapter 2')
    # print(seg.osis())
