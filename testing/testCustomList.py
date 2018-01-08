import unittest

from utils.CustomList import CustomList


class CustomListTest(unittest.TestCase):
    def __key(self, a, b):  # key for sorting
        return a > b

    def f(self, x): # filter criterion
        return x<4

    def setUp(self):
        self.l = CustomList(int)
        self.l.append(1)
        self.l.append(5)
        self.l.append(4)
        self.l.append(2)
        self.l.append(0)
        self.l.append(3)

    def testSort(self):
        self.l.sort(self.__key)

        for i in range(6):
            self.assertEqual(self.l[i], i)

    def testGetAssign(self):

        self.l[3] = 0
        self.assertEqual(self.l[3], 0)
        self.assertRaises(TypeError, lambda: self.l.append("TestString"))

    def testLen(self):
        self.assertEqual(len(self.l), 6)

    def testDelete(self):
        del self.l[1]

        self.assertEqual(len(self.l), 5)
        self.assertEqual(self.l[1], 4)

        self.l.pop(1)
        self.assertEqual(len(self.l), 4)

    def testToString(self):
        self.assertEqual(str(self.l), "[1, 5, 4, 2, 0, 3]")

    def testIterator(self):
        iterator = iter(self.l)
        while True:
            try:
                elem = next(iterator)
            except StopIteration:
                break

    def testFilterSort(self):
        expected = [0, 1, 2, 3]
        lst = self.l.filter(self.f)
        lst.sort(self.__key)
        self.assertEqual(str(lst), str(expected))
