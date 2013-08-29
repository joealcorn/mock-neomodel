from mock_neomodel.core import FakeNode
from mock_neomodel.relationship_manager import FakeRelation


class FakeLocalised(object):
    def __init__(self, *args, **kwargs):
        super(FakeLocalised, self).__init__(*args, **kwargs)
        self.locales = FakeRelation(self)

    def add_locale(self, lang):
        self.locales.connect(FakeNode(code=lang).save())

    def remove_locale(self, lang):
        self.locales.disconnect(FakeNode.index.get(code=lang))

    def has_locale(self, lang):
        self.locales.is_connected(FakeNode.index.get(code=lang))
