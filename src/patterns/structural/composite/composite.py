# Composite Pattern
# The composite pattern allows to treat single objects and composite of objects in the
# same way, providing a unified interface for both cases.
from abc import ABC
from typing import Iterable


class GraphicObject:
    def __init__(self, color=None):
        self._name = "Group"
        self.color = color
        self.children = []

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f"{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs"

    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f"{name}-{x}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":
    # in this case, the Composite Pattern is implemented through the GraphicObject class
    # since it can be both a single object and a composite of objects of the same class
    # by means of the children attribute
    # drawing = GraphicObject()
    # drawing._name = "My Drawing"
    # drawing.children.append(Circle("Blue"))
    # drawing.children.append(Square("Red"))
    #
    # group = GraphicObject()
    # group.children.append(Circle("Green"))
    # group.children.append(Square("Green"))
    # drawing.children.append(group)
    #
    # print(drawing)
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)
