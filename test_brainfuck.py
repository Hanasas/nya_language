#!/usr/bin/env python3

import unittest
from brainfuck import BrainfuckInterpreter

class TestBrainfuckInterpreter(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = BrainfuckInterpreter()
    
    def test_hello_world(self):
        code = """
        ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>
        ---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
        """
        result = self.interpreter.run(code)
        self.assertEqual(result, "Hello World!\n")
    
    def test_addition(self):
        code = ",>,<[>+<-]>."
        result = self.interpreter.run(code, "\x02\x03")
        self.assertEqual(result, chr(5))
    
    def test_memory_operations(self):
        code = "+++>++>+<<<[>+<-]>[>+<-]>."
        result = self.interpreter.run(code)
        self.assertEqual(result, chr(5))
    
    def test_loop(self):
        code = "+++[>++<-]>."
        result = self.interpreter.run(code)
        self.assertEqual(result, chr(6))
    
    def test_nested_loops(self):
        code = "+++++[>+++++[>++<-]<-]>>."
        result = self.interpreter.run(code)
        self.assertEqual(result, chr(50))
    
    def test_input_output(self):
        code = ",.,."
        result = self.interpreter.run(code, "AB")
        self.assertEqual(result, "AB")
    
    def test_pointer_movement(self):
        code = "+++>++<[>+<-]>."
        result = self.interpreter.run(code)
        self.assertEqual(result, chr(5))
    
    def test_zero_cell(self):
        code = "+++[-]."
        result = self.interpreter.run(code)
        self.assertEqual(result, chr(0))
    
    def test_alphabet(self):
        code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
        result = self.interpreter.run(code)
        self.assertEqual(result, "Hello World!\n")

if __name__ == '__main__':
    unittest.main()