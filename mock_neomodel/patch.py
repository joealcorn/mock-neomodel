from fudge import patch_object as fudge_patch

from mock_neomodel import FakeNode, FakeIndex, FakeRelation


def patch():
    """
    patches neomodel objs
    """
    import neomodel
    fudge_patch(neomodel, 'StructuredNode', FakeNode)
    fudge_patch(neomodel, 'NodeIndexManager', FakeIndex)
    fudge_patch(neomodel, 'RelationshipManager', FakeRelation)
