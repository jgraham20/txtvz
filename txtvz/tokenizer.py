# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

import re
from collections import namedtuple
Token = namedtuple('Token', ['typ', 'value', 'line', 'column'])

class Grammar:

    def __init__(self, rules=('ANY', r'.')):
        self.tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in rules)


class TokenStream:

    token_specification = [
            ('NUMBER',  r'\d+(\.\d*)?'),  # Integer or decimal number
            ('WORD',      r'\w+'),    # Identifiers
            ('WS', r'[ \n\t]+'),           # Line endings
            ('PUNC', r'[\u2000-\u206F\u2E00-\u2E7F\\!"#$%&()*+,\-.\/:;<=>?@\[\]^_`{|}~]'),
            ('UNMATCHED',r'.'),            # Any other character
        ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tok_regex = re.compile(tok_regex)

    def tokenize(self, t):

        for mo in re.finditer(self.tok_regex, t):
            kind = mo.lastgroup
            value = mo.group(kind)
            start = mo.start(kind)
            end = mo.end(kind)
            yield Token(kind, value, start, end)
