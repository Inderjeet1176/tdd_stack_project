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
    def test_push_multiple_items(self):
        stack = MyStack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertFalse(stack.is_empty()) 
        self.assertEqual(stack.peek(), 30)  
    def test_pop_from_stack(self):
        stack = MyStack()
        stack.push(10)
        popped_item = stack.pop()

        self.assertEqual(popped_item, 10)  
        self.assertTrue(stack.is_empty())  
    def test_pop_from_empty_stack(self):
        stack = MyStack()

        with self.assertRaises(IndexError):  
            stack.pop()
    


