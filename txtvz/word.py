# -*- coding: utf-8 -*-


class Word:

    def __init__(self, token):
        self.token = token
        self.right = []

    def append(self, word):
        self.right.append(word)

    def __repr__(self):
        return self.token + ' - '.join(x for x in self.right)
