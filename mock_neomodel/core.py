from fudge import Fake
from neomodel.exception import DoesNotExist
from .index import FakeIndex
from .relationship_manager import FakeCategoryRelation

INDEX_REGISTER = []


class FakeCategoryNode(object):
    def __init__(self, index):
        self.instance = FakeCategoryRelation(self, index.nodes)


def factory_reset():
    for index in INDEX_REGISTER:
        index._reset()


class FakeNodeMeta(type):
    def __new__(mcs, name, bases, dct):
        inst = super(FakeNodeMeta, mcs).__new__(mcs, name, bases, dct)
        inst.index = FakeIndex()
        INDEX_REGISTER.append(inst.index)
        return inst

FakeNodeBase = FakeNodeMeta('NodeBase', (), {})


class FakeNode(FakeNodeBase):
    DoesNotExist = DoesNotExist

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
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

    @classmethod
    def category(cls):
        return FakeCategoryNode(cls.index)
