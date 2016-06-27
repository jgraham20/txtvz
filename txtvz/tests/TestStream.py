# -*- coding: utf-8 -*-

# pylint: disable=W0614,W0401,W0611
# flake8: noqa

import unittest
import re
from txtvz import tokenizer

class SimpleTokenTest(unittest.TestCase):

    tokenizer = None
    text = """Sometimes the Bible refers to the Son of God as "the Word of God." In Revelation 19:13, John sees the risen Lord Jesus in heaven and says, "The name by which he is called is The Word of God." Similarly, in the beginning of John's gospel we read, "In the beginning was the Word, and the Word was with God, and the Word was God" (John 1:1). It is clear that John is speaking of the Son of God here, because in verse 14 he says, "And the Word became flesh and dwelt among us, full of grace and truth; we have beheld his glory, glory as of the only Son from the Father." These verses (and perhaps 1 John 1:1) are the only instances where the Bible refers to God the Son as "the Word" or "the Word of God," so this usage is not common. But it does indicate that among the members of the Trinity it is especially God the Son who in his person as well as in his words has the role of communicating the character of God to us and of expressing the will of God for us.
"""


    def setUp(self):
        self.tokenizer = tokenizer.TokenStream()

    def test_token_stream(self):

        for s in self.tokenizer.tokenize(self.text):
            print(s)
