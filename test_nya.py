#!/usr/bin/env python3

import unittest
from nya import NyaInterpreter

class TestNyaInterpreter(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = NyaInterpreter()
    
    def test_tokenization(self):
        nya_code = "meow miao nya yaong miaou miau miyav meom"
        tokens = self.interpreter.tokenize(nya_code)
        expected = ['meow', 'miao', 'nya', 'yaong', 'miaou', 'miau', 'miyav', 'meom']
        self.assertEqual(tokens, expected)
    
    def test_nya_to_brainfuck(self):
        nya_code = "meow miao nya yaong miaou miau miyav meom"
        bf_code = self.interpreter.nya_to_brainfuck(nya_code)
        self.assertEqual(bf_code, "[><.+-,]")
    
    def test_brainfuck_to_nya(self):
        bf_code = "[><.+-,]"
        nya_code = self.interpreter.brainfuck_to_nya(bf_code)
        expected = "meow miao nya yaong miaou miau miyav meom"
        self.assertEqual(nya_code, expected)
    
    def test_case_insensitive(self):
        nya_code = "MEOW MIAO NYA YAONG MIAOU MIAU MIYAV MEOM"
        bf_code = self.interpreter.nya_to_brainfuck(nya_code)
        self.assertEqual(bf_code, "[><.+-,]")
    
    def test_ignore_invalid_tokens(self):
        nya_code = "meow hello miao world nya"
        tokens = self.interpreter.tokenize(nya_code)
        self.assertEqual(tokens, ['meow', 'miao', 'nya'])
    
    def test_simple_output(self):
        nya_code = "miaou miaou miaou miaou miaou yaong"
        result = self.interpreter.run(nya_code)
        self.assertEqual(result, chr(5))
    
    def test_loop(self):
        nya_code = "miaou miaou miaou meow miao miaou miaou nya miau meom miao yaong"
        result = self.interpreter.run(nya_code)
        self.assertEqual(result, chr(6))
    
    def test_validate_brackets_valid(self):
        nya_code = "meow miao meow nya meom meom"
        valid, msg = self.interpreter.validate_brackets(nya_code)
        self.assertTrue(valid)
    
    def test_validate_brackets_unmatched_meow(self):
        nya_code = "meow miao meow nya meom"
        valid, msg = self.interpreter.validate_brackets(nya_code)
        self.assertFalse(valid)
        self.assertIn("Unmatched 'meow'", msg)
    
    def test_validate_brackets_unmatched_meom(self):
        nya_code = "miao meow nya meom meom"
        valid, msg = self.interpreter.validate_brackets(nya_code)
        self.assertFalse(valid)
        self.assertIn("Unmatched 'meom'", msg)
    
    def test_addition(self):
        nya_code = "miyav miao miyav nya meow miao miaou nya miau meom miao yaong"
        result = self.interpreter.run(nya_code, "\x02\x03")
        self.assertEqual(result, chr(5))
    
    def test_hello_world_simple(self):
        nya_code = """
        miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou
        meow miao miaou miaou miaou miaou miaou miaou miaou nya miau meom
        miao miaou miaou yaong
        """
        result = self.interpreter.run(nya_code)
        self.assertEqual(result, 'H')
    
    def test_echo(self):
        nya_code = "miyav yaong miyav yaong"
        result = self.interpreter.run(nya_code, "AB")
        self.assertEqual(result, "AB")
    
    def test_format_code(self):
        nya_code = "meow miao meow nya meom meom"
        formatted = self.interpreter.format_nya_code(nya_code)
        expected = "meow\n  miao\n  meow\n    nya\n  meom\nmeom"
        self.assertEqual(formatted, expected)
    
    def test_memory_operations(self):
        nya_code = "miaou miaou miaou miao miaou miaou nya meow miao miaou nya miau meom miao yaong"
        result = self.interpreter.run(nya_code)
        self.assertEqual(result, chr(5))

class TestNyaEdgeCases(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = NyaInterpreter()
    
    def test_empty_code(self):
        result = self.interpreter.run("")
        self.assertEqual(result, "")
    
    def test_only_whitespace(self):
        result = self.interpreter.run("   \n\n\t  ")
        self.assertEqual(result, "")
    
    def test_no_valid_tokens(self):
        result = self.interpreter.run("hello world cat dog")
        self.assertEqual(result, "")
    
    def test_mixed_with_comments(self):
        nya_code = "miaou miaou # this is a comment\n yaong"
        result = self.interpreter.run(nya_code)
        self.assertEqual(result, chr(2))
    
    def test_nested_loops(self):
        nya_code = """
        miaou miaou miaou
        meow
          miao miaou miaou
          meow
            miao miaou
            nya miau
          meom
          nya miau
        meom
        miao miao yaong
        """
        result = self.interpreter.run(nya_code)
        self.assertEqual(result, chr(6))

if __name__ == '__main__':
    unittest.main()