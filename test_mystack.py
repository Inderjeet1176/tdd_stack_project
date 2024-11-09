import unittest
from mystack import MyStack

class TestMyStack(unittest.TestCase):
    def test_create_empty_stack(self):
        stack = MyStack()
        self.assertTrue(stack.is_empty())
    def test_push_to_stack(self):
        stack = MyStack()
        stack.push(10)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(), 10)


