#!/usr/bin/env python3

from nya import NyaInterpreter

def main():
    print("=== Nya Language Demo ===\n")
    print("Nya是一门猫咪友好的编程语言 (=^･ω･^=)\n")
    
    interpreter = NyaInterpreter()
    
    # 示例1：输出字符
    print("1. 输出字符 'A':")
    print("   代码: " + "miaou " * 65 + "yaong")
    nya_code = "miaou " * 65 + "yaong"
    result = interpreter.run(nya_code)
    print(f"   输出: {result}\n")
    
    # 示例2：简单循环
    print("2. 使用循环输出 '0':")
    nya_code = "miaou miaou miaou miaou miaou miaou meow miao miaou miaou miaou miaou miaou miaou miaou miaou nya miau meom miao yaong"
    print(f"   代码: {nya_code}")
    result = interpreter.run(nya_code)
    print(f"   输出: {result}\n")
    
    # 示例3：Brainfuck转Nya
    print("3. Brainfuck转Nya:")
    bf_code = "++++++[>++++++++<-]>."
    print(f"   Brainfuck: {bf_code}")
    nya_code = interpreter.brainfuck_to_nya(bf_code)
    print(f"   Nya: {nya_code}")
    result = interpreter.run(nya_code)
    print(f"   输出: {result}\n")
    
    # 示例4：代码格式化
    print("4. 代码格式化:")
    nya_code = "meow miao miaou meow nya miau meom meom"
    print(f"   原始代码: {nya_code}")
    formatted = interpreter.format_nya_code(nya_code)
    print("   格式化后:")
    for line in formatted.split('\n'):
        print(f"     {line}")
    print()
    
    # 示例5：括号验证
    print("5. 语法验证:")
    valid_code = "meow miao meom"
    invalid_code = "meow miao meow meom"
    
    valid, msg = interpreter.validate_brackets(valid_code)
    print(f"   代码: {valid_code}")
    print(f"   验证结果: {'✓ 有效' if valid else '✗ 无效'} - {msg}")
    
    valid, msg = interpreter.validate_brackets(invalid_code)
    print(f"   代码: {invalid_code}")
    print(f"   验证结果: {'✓ 有效' if valid else '✗ 无效'} - {msg}")
    
    print("\n=== Demo完成 ===")
    print("Nya~ Nya~ (=^･ω･^=)")

if __name__ == "__main__":
    main()