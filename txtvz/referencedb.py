# -*- coding: utf-8 -*-


class ReferenceDB:

    STATE_INSERT = 0
    STATE_CONTINUE = 1

    def __init__(self, book=None):
        self.current_state = ReferenceDB.STATE_INSERT
        self.symbol_table = {}
        self.book = book

    def add_book(self, book):
        """
        Add book to the referenceDB.
        The last book node added will become the current book node.
        :param self
        :param book
        """
        return None

    def add_node(self, node):
        s = self.symbol(node)
        print(s)

    def draw_edge(self, node):
        s = self.symbol(node)
        print(s)

    def build_reference(self, text):

        self.text = text

    def set_book(self, book):
            self.book = book

    def add_chapter(self, chapter):
            self.chapter = chapter

    def symbol(self, token_id):
        """
        Get symbol from the symbol table
        :param self
        :param token_id
        :return: symbol
        >>> r = ReferenceDB()
        >>> a = r.symbol("Gen")
        >>> b = r.symbol("Gen")
        >>> c = r.symbol("XXX")
        >>> assert a == b
        >>> assert a!=c
        """
        try:
            s = self.symbol_table[token_id]
        except KeyError:
            class s(object):
                pass

            s.__name__ = "symbol-" + token_id  # for debugging
            s.token_id = token_id
            s.token_value = None
            s.token_type = None
            s.child = []
            s.right = []

            self.symbol_table[token_id] = s

        return s

if __name__ == "__main__":
    import doctest
    doctest.testmod()
