#!/usr/bin/env python3

import sys
import re
from typing import Dict, Tuple
from brainfuck import BrainfuckInterpreter

class NyaInterpreter:
    def __init__(self, memory_size: int = 30000):
        self.bf_interpreter = BrainfuckInterpreter(memory_size)
        self.nya_to_bf = {
            'meow': '[',
            'miao': '>',
            'nya': '<',
            'yaong': '.',
            'miaou': '+',
            'miau': '-',
            'miyav': ',',
            'meom': ']'
        }
        self.bf_to_nya = {v: k for k, v in self.nya_to_bf.items()}
        
    def tokenize(self, code: str) -> list:
        sorted_keywords = sorted(self.nya_to_bf.keys(), key=len, reverse=True)
        pattern = '|'.join(re.escape(keyword) for keyword in sorted_keywords)
        tokens = re.findall(pattern, code.lower())
        return tokens
    
    def nya_to_brainfuck(self, nya_code: str) -> str:
        tokens = self.tokenize(nya_code)
        bf_code = ''.join(self.nya_to_bf.get(token, '') for token in tokens)
        return bf_code
    
    def brainfuck_to_nya(self, bf_code: str) -> str:
        nya_tokens = []
        for char in bf_code:
            if char in self.bf_to_nya:
                nya_tokens.append(self.bf_to_nya[char])
        return ' '.join(nya_tokens)
    
    def run(self, nya_code: str, input_data: str = "") -> str:
        bf_code = self.nya_to_brainfuck(nya_code)
        return self.bf_interpreter.run(bf_code, input_data)
    
    def validate_brackets(self, nya_code: str) -> Tuple[bool, str]:
        tokens = self.tokenize(nya_code)
        stack = []
        position = 0
        
        for token in tokens:
            if token == 'meow':
                stack.append(position)
            elif token == 'meom':
                if not stack:
                    return False, f"Unmatched 'meom' at position {position}"
                stack.pop()
            position += 1
        
        if stack:
            return False, f"Unmatched 'meow' at position {stack[0]}"
        
        return True, "Valid nya code"
    
    def format_nya_code(self, nya_code: str, indent_size: int = 2) -> str:
        tokens = self.tokenize(nya_code)
        formatted = []
        indent_level = 0
        
        for token in tokens:
            if token == 'meom':
                indent_level -= 1
                
            formatted.append(' ' * (indent_level * indent_size) + token)
            
            if token == 'meow':
                indent_level += 1
        
        return '\n'.join(formatted)

class NyaREPL:
    def __init__(self):
        self.interpreter = NyaInterpreter()
        self.history = []
        
    def run(self):
        print("Nya Language Interactive REPL")
        print("Type 'help' for commands, 'exit' to quit")
        print("~" * 40)
        
        while True:
            try:
                line = input("nya> ").strip()
                
                if not line:
                    continue
                    
                if line == 'exit':
                    print("Sayonara~ (=^･ω･^=)")
                    break
                    
                elif line == 'help':
                    self.show_help()
                    
                elif line == 'keywords':
                    self.show_keywords()
                    
                elif line == 'history':
                    self.show_history()
                    
                elif line.startswith('bf '):
                    bf_code = line[3:]
                    nya_code = self.interpreter.brainfuck_to_nya(bf_code)
                    print(f"Nya: {nya_code}")
                    
                else:
                    valid, msg = self.interpreter.validate_brackets(line)
                    if not valid:
                        print(f"Error: {msg}")
                        continue
                        
                    self.history.append(line)
                    result = self.interpreter.run(line)
                    if result:
                        print(result, end='')
                        
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit")
            except Exception as e:
                print(f"Error: {e}")
    
    def show_help(self):
        print("\nCommands:")
        print("  help     - Show this help message")
        print("  keywords - Show nya language keywords")
        print("  history  - Show command history")
        print("  bf <code> - Convert Brainfuck to Nya")
        print("  exit     - Exit REPL")
        print()
        
    def show_keywords(self):
        print("\nNya Language Keywords:")
        print("  meow  - [ (start loop)")
        print("  miao  - > (move pointer right)")
        print("  nya   - < (move pointer left)")
        print("  yaong - . (output)")
        print("  miaou - + (increment)")
        print("  miau  - - (decrement)")
        print("  miyav - , (input)")
        print("  meom  - ] (end loop)")
        print()
        
    def show_history(self):
        print("\nCommand History:")
        for i, cmd in enumerate(self.history, 1):
            print(f"  {i}: {cmd}")
        print()

def main():
    if len(sys.argv) < 2:
        repl = NyaREPL()
        repl.run()
        return
    
    interpreter = NyaInterpreter()
    
    if sys.argv[1] == '-c':
        if len(sys.argv) < 3:
            print("Error: No code provided")
            sys.exit(1)
        code = sys.argv[2]
        input_data = sys.argv[3] if len(sys.argv) > 3 else ""
        
    elif sys.argv[1] == '-t':
        if len(sys.argv) < 3:
            print("Error: No code provided for translation")
            sys.exit(1)
        bf_code = sys.argv[2]
        nya_code = interpreter.brainfuck_to_nya(bf_code)
        print("Nya translation:")
        print(nya_code)
        return
        
    elif sys.argv[1] == '-f':
        if len(sys.argv) < 3:
            print("Error: No file provided")
            sys.exit(1)
        try:
            with open(sys.argv[2], 'r') as f:
                code = f.read()
            formatted = interpreter.format_nya_code(code)
            print(formatted)
            return
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
            
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                code = f.read()
            input_data = sys.argv[2] if len(sys.argv) > 2 else ""
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    
    valid, msg = interpreter.validate_brackets(code)
    if not valid:
        print(f"Syntax Error: {msg}")
        sys.exit(1)
    
    try:
        interpreter.run(code, input_data)
        print()
    except Exception as e:
        print(f"Runtime Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()