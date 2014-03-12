from neomodel.exception import DoesNotExist


class FakeIndex(object):
    def __init__(self):
        self.nodes = {}
        self.last = 0

    def _reset(self):
        self.nodes = {}
        self.last = 0

    def search(self, **kwargs):
        results = []
        for node in self.nodes.values():
            match = True
            for (key, value) in kwargs.iteritems():
                if not hasattr(node, key) or getattr(node, key) != value:
                    match = False
                    break
            if match:
                results.append(node)
        return results

    def get(self, **kwargs):
        for node in self.nodes.itervalues():
            match = True
            for (key, value) in kwargs.iteritems():
                if not hasattr(node, key) or getattr(node, key) != value:
                    match = False
                    break
            if match:
                return node
        raise DoesNotExist(
            "Node with attributes %s doesn't exist in index." % kwargs
        )

    def register(self, node):
        self.nodes[node._id] = node

    def __str__(self):
        ''' Helper printing function for debugging the index '''
        result = ''
        for k, v in self.nodes.items():
            result += str(k) + ': \n'
            for attr in vars(v):
                result += '\t' + str(attr) + ' = ' + str(getattr(v, attr)) + '\n'
        return result

    def delete(self, uid):
        del self.nodes[uid]
