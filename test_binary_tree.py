import unittest
import binary_tree
import io
import sys

class Test(unittest.TestCase):
    tree = binary_tree.BinaryTree(70)
    list = [31,93,14, 73,94,23]
    for x in list:
        tree.insert(x)

    def test_1_(self):
        print("\nRunning test1: find")
        self.assertTrue(self.tree.find(94))
        self.assertFalse(self.tree.find(74))
    def test_2_(self):
        print("\nRunning test2: insert")
        self.tree.insert(11)
        self.assertTrue(self.tree.find(11))
    def test_3_(self):
        print("\nRunning test3: pre-order traversal (print)")
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        self.tree.traversePreOrder()                                  
        sys.stdout = sys.__stdout__                     
        result = capturedOutput.getvalue()
        self.assertEqual(result,'70 31 14 11 23 93 73 94 ')
    def test_4_(self):
        print("\nRunning test4: delete")
        self.tree.delete(14)
        self.assertFalse(self.tree.find(14))
    def test_5_(self):
        print("\nRunning test5: not empty")
        self.assertTrue(self.tree.isEmpty())
    def test_6_(self):
        print("\nRunning test6: empty")
        self.tree.delete(70)
        self.assertTrue(self.tree.isEmpty())
if __name__ == '__main__':
    unittest.main()