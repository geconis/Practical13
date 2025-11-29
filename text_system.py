class TextElement:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, name):
        self.children = [c for c in self.children if c.name != name]


class TextContext:
    def __init__(self):
        self.root = TextElement("root")
        self.current = self.root

    def pwd(self):
        path = []
        elem = self.current
        while elem:
            path.append(elem.name)
            elem = elem.parent
        return "/" + "/".join(reversed(path))

    def print_elem(self, whole=False):
        if whole:
            def recurse(elem, level=0):
                out = "  " * level + elem.name + "\n"
                for child in elem.children:
                    out += recurse(child, level + 1)
                return out
            return recurse(self.root)
        else:
            return self.current.name
