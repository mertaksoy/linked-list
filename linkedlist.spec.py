import unittest

from linkedlist import LinkedList, Node


class LinkedListSpec(unittest.TestCase):

    def test_linked_list_size(self):
        llist = LinkedList()
        llist.add_first(Node("a"))
        llist.add_first(Node("b"))
        llist.add_first(Node("c"))
        self.assertEqual(len(list(llist)), 3)

    def test_linked_list_head(self):
        llist = LinkedList()
        llist.add_first(Node("a"))
        llist.add_first(Node("b"))
        self.assertEqual(str(llist.head), "b")


if __name__ == '__main__':
    unittest.main()
