from neomodel.exception import DoesNotExist


class FakeRelation(object):
    def __init__(self, origin):
        self.origin = origin
        self.connections = {}
        self.relation_properties = {}

    def __bool__(self):
        return len(self.connections) > 0

    def __len__(self):
        return len(self.connections)

    def __nonzero__(self):
        return len(self.connections) > 0

    def search(self, **kwargs):
        results = []
        for node in self.connections.values():
            match = True
            for (key, value) in kwargs.iteritems():
                if not hasattr(node, key) or getattr(node, key) != value:
                    match = False
                    break
            if match:
                results.append(node)
        return results

    def get(self, **kwargs):
        for n in self.connections.values():
            found = True
            for key in kwargs.keys():
                if not getattr(n, key, None) == kwargs[key]:
                    found = False
            if found:
                return n
        raise DoesNotExist

    def connect(self, node, properties=None):
        self.connections[node._id] = node
        if properties is not None and isinstance(properties, dict):
            self.relation_properties[node._id] = properties

    def disconnect(self, node):
        del self.connections[node._id]

    def reconnect(self, node, new_node):
        del self.connections[node._id]
        self.connections[new_node._id] = new_node

    def all(self):
        return self.connections.values()

    def single(self):
        if self.connections.values():
            return self.connections.values()[0]
        else:
            return None

    def count(self):
        return len(self.connections)

    def is_connected(self, node):
        return node._id in self.connections


class FakeCategoryRelation(FakeRelation):
    def __init__(self, origin, nodes):
        super(FakeCategoryRelation, self).__init__(origin)
        self.connections = nodes

    def connect(self, *args, **kwargs):
        raise NotImplemented("Not available on category node rel")

    def reconnect(self, *args, **kwargs):
        raise NotImplemented("Not available on category node rel")

    def disconnect(self, *args, **kwargs):
        raise NotImplemented("Not available on category node rel")

    def single(self, *args, **kwargs):
        raise NotImplemented("Not available on category node rel")

    def is_connected(self, *args, **kwargs):
        raise NotImplemented("Not available on category node rel")
