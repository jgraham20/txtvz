# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

class WordVec:

    def __init__(self):
        self.words = {}

    def push(self, c):
        self.words.update(c)
