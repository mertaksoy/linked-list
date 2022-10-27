class Node:
    """
    The Node class to represent a node of the list
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    """
    The LinkedList class to build a list from nodes
    """

    def __init__(self):
        """
        The initialization of the list
        """
        self.head = None

    def __iter__(self):
        """
        Validate and yield every single node
        :return:
        """
        _node = self.head
        while _node is not None:
            yield _node
            _node = _node.next

    def __repr__(self):
        _node = self.head
        nodes = []
        while _node is not None:
            nodes.append(_node.data)
            _node = _node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, _node):
        """
        Adds the node at the first position of the list
        :param _node: Node
        """
        _node.next = self.head
        self.head = _node
