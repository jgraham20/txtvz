# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

import re
from collections import namedtuple
Token = namedtuple('Token', ['typ', 'value', 'line', 'column'])

class Grammar:

    def __init__(self, rules=None):
        if rules is None:
            rules = [('WORD', r'(?ms)([a-zA-Z]+)'),
                     ('PUNC', r'[:\.,]'),
                     ('DIGIT', r'\d+'),
                     ('CONT', r'[-]')
                     ]
        self.tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in rules)

class TokenStream:

    def __init__(self, grammar):
        self.token_specification = grammar
        self.tok_regex = re.compile(grammar.tok_regex)

    def tokenize(self, t):

        for mo in re.finditer(self.tok_regex, t):
            kind = mo.lastgroup
            value = mo.group(kind)
            start = mo.start(kind)
            end = mo.end(kind)
            yield Token(kind, value, start, end)

if __name__ == '__main__':
    g = Grammar()
    t = TokenStream(g)
    for seg in t.tokenize('The Gospel according to Saint Mark 1:1-2'):
        print(seg)