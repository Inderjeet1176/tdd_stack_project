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
    def test_peek_on_empty_stack(self):
        stack = MyStack()

        self.assertIsNone(stack.peek())  
    def test_stack_size(self):
        stack = MyStack()
        self.assertEqual(stack.size(), 0)  
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.size(), 2)  
    def test_push_and_pop_multiple_items(self):
        stack = MyStack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        popped_item = stack.pop()
        self.assertEqual(popped_item, 30)
       
        popped_item = stack.pop()
        self.assertEqual(popped_item, 20)
        
        popped_item = stack.pop()
        self.assertEqual(popped_item, 10)
        
        self.assertTrue(stack.is_empty())

    def test_stack_after_push_pop_operations(self):
        stack = MyStack()
        stack.push(10)
        stack.push(20)
        stack.pop()       
        stack.push(30)      
        self.assertEqual(stack.peek(), 30)       
        self.assertEqual(stack.size(), 2)

    def test_pop_and_push_same_element(self):
        stack = MyStack()
        stack.push(10)
        popped_item = stack.pop()
        self.assertEqual(popped_item, 10)
        stack.push(10)
        self.assertEqual(stack.peek(), 10)

    def test_multiple_pops_from_stack(self):
        stack = MyStack()
        stack.push(10)
        stack.push(20)
        stack.pop()
        stack.pop()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_stack_order(self):
        stack = MyStack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.pop(), 30)  
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)  

    def test_stack_size_after_push_pop(self):
        stack = MyStack()
        stack.push(10)
        self.assertEqual(stack.size(), 1)
        stack.push(20)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.push(30)
        self.assertEqual(stack.size(), 2)
    
        
    
    
        





