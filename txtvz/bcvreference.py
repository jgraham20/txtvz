# -*- coding: utf-8 -*-


class Reference(object):

    def __init__(self, text=None):
        self.text = text
        self.ref_type = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_ref_type(self, type):
        self.ref_type = type
