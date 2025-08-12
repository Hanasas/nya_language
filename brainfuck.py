#!/usr/bin/env python3

import sys
from typing import List, Dict

class BrainfuckInterpreter:
    def __init__(self, memory_size: int = 30000):
        self.memory = [0] * memory_size
        self.pointer = 0
        self.instruction_pointer = 0
        self.output = []
        self.input_buffer = []
        
    def _find_matching_bracket(self, code: str, start: int, direction: int) -> int:
        depth = 1
        i = start + direction
        
        while 0 <= i < len(code) and depth > 0:
            if code[i] == '[':
                depth += 1 if direction > 0 else -1
            elif code[i] == ']':
                depth += -1 if direction > 0 else 1
            i += direction
            
        return i - direction if depth == 0 else -1
    
    def _build_jump_table(self, code: str) -> Dict[int, int]:
        jump_table = {}
        stack = []
        
        for i, char in enumerate(code):
            if char == '[':
                stack.append(i)
            elif char == ']':
                if stack:
                    left = stack.pop()
                    right = i
                    jump_table[left] = right
                    jump_table[right] = left
                    
        return jump_table
    
    def run(self, code: str, input_data: str = ""):
        self.input_buffer = list(input_data)
        self.instruction_pointer = 0
        self.output = []
        
        jump_table = self._build_jump_table(code)
        
        while self.instruction_pointer < len(code):
            instruction = code[self.instruction_pointer]
            
            if instruction == '>':
                self.pointer = (self.pointer + 1) % len(self.memory)
                
            elif instruction == '<':
                self.pointer = (self.pointer - 1) % len(self.memory)
                
            elif instruction == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
                
            elif instruction == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
                
            elif instruction == '.':
                self.output.append(chr(self.memory[self.pointer]))
                print(chr(self.memory[self.pointer]), end='')
                
            elif instruction == ',':
                if self.input_buffer:
                    self.memory[self.pointer] = ord(self.input_buffer.pop(0))
                else:
                    try:
                        char = sys.stdin.read(1)
                        if char:
                            self.memory[self.pointer] = ord(char)
                        else:
                            self.memory[self.pointer] = 0
                    except:
                        self.memory[self.pointer] = 0
                        
            elif instruction == '[':
                if self.memory[self.pointer] == 0:
                    self.instruction_pointer = jump_table.get(self.instruction_pointer, self.instruction_pointer)
                    
            elif instruction == ']':
                if self.memory[self.pointer] != 0:
                    self.instruction_pointer = jump_table.get(self.instruction_pointer, self.instruction_pointer)
            
            self.instruction_pointer += 1
        
        return ''.join(self.output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python brainfuck.py <filename> [input]")
        print("   or: python brainfuck.py -c <code> [input]")
        sys.exit(1)
    
    interpreter = BrainfuckInterpreter()
    
    if sys.argv[1] == '-c':
        if len(sys.argv) < 3:
            print("Error: No code provided")
            sys.exit(1)
        code = sys.argv[2]
        input_data = sys.argv[3] if len(sys.argv) > 3 else ""
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
    
    interpreter.run(code, input_data)
    print()

if __name__ == "__main__":
    main()