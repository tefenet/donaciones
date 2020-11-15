import math

from flask import render_template


class Page(object):

    def __init__(self, query, page, page_size, criteria=None):
        if page <= 0:
            raise AttributeError('page needs to be >= 1')
        if page_size <= 0:
            raise AttributeError('page_size needs to be >= 1')
        self.current = page
        self.items = query.order_by(criteria).limit(page_size).offset((page - 1) * page_size).all()
        self.total = query.count()
        self.page_size = page_size

    def previous_page(self):
        if self.has_previous():
            return self.current - 1
        else:
            return None

    def next_page(self):
        if self.has_next:
            return self.current + 1
        else:
            return None

    def pages(self):
        return int(math.ceil(self.total / float(self.page_size)))

    def has_previous(self):
        return self.current > 1

    def has_next(self):
        previous_items = (self.current - 1) * self.page_size
        return previous_items + len(self.items) < self.total
