from fudge import Fake
from neomodel.exception import DoesNotExist

from .index import FakeIndex


class FakeNode(object):
    DoesNotExist = DoesNotExist

    index = FakeIndex()

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
            #print 'set %s : %s' % (key, value)
        self._id = self.index.last
        self.index.last += 1
        for node_id, node in self.__class__.index.nodes.iteritems():
            if node.__str__() == self.__str__():
                self._id = node_id
        self.index.last += 1

    def save(self):
        self.__class__.index.register(self)
        self.__node__ = Fake('__node__').has_attr(id=self._id)
        return self

    def delete(self):
        self.index.delete(self._id)
        # TODO: delete relationships
        del self

    def cypher(self, query, params=None):
        pass
