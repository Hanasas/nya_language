# Brainfuck解释器

一个用Python实现的Brainfuck编程语言解释器。

## 特性

- 完整实现8个Brainfuck指令
- 支持嵌套循环
- 30000个内存单元
- 命令行接口
- 从文件或直接从命令行运行代码

## Brainfuck指令

- `>` - 指针右移
- `<` - 指针左移  
- `+` - 当前单元格值加1
- `-` - 当前单元格值减1
- `.` - 输出当前单元格的ASCII字符
- `,` - 读取输入存入当前单元格
- `[` - 如果当前单元格值为0，跳转到对应的`]`后
- `]` - 如果当前单元格值非0，跳转到对应的`[`后

## 使用方法

### 从文件运行
```bash
python brainfuck.py filename.bf [input]
```

### 直接运行代码
```bash
python brainfuck.py -c "brainfuck_code" [input]
```

### 示例

Hello World:
```bash
python brainfuck.py -c "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
```

### 作为Python模块使用
```python
from brainfuck import BrainfuckInterpreter

interpreter = BrainfuckInterpreter()
result = interpreter.run("++++++[>++++++++<-]>.")
print(result)  # 输出 '0'
```

## 测试

运行测试套件:
```bash
python test_brainfuck.py
```