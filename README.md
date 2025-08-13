# 🐱 Nya Language - 猫咪编程语言

<div align="center">
  
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
  [![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
  [![Test Status](https://img.shields.io/badge/tests-passing-brightgreen)](./test_nya.py)
  
  **Nya** 是一门基于 Brainfuck 的猫咪友好编程语言，使用萌萌的猫叫声作为关键字！
  
  `meow` `miao` `nya` `yaong` `miaou` `miau` `miyav` `meom`
  
  *让编程变得更加可爱！* (=^･ω･^=)
</div>

---

## 📖 目录

- [快速开始](#-快速开始)
- [安装](#-安装)
- [语言特性](#-语言特性)
- [语法说明](#-语法说明)
- [使用方法](#-使用方法)
- [示例程序](#-示例程序)
- [API文档](#-api文档)
- [测试](#-测试)
- [贡献指南](#-贡献指南)
- [FAQ](#-faq)
- [许可证](#-许可证)

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/nya.git
cd nya

# 2. 运行Hello World
python nya.py examples/hello_world.nya

# 3. 进入交互式环境
python nya.py
>>> miaou miaou miaou miaou miaou yaong  # 输出 ASCII 5
```

## 📦 安装

### 系统要求

- Python 3.6 或更高版本
- 支持 Windows、macOS 和 Linux

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/nya.git
   cd nya
   ```

2. **验证安装**
   ```bash
   python nya.py -c "miaou miaou miaou yaong"  # 应该输出 ASCII 3
   ```

3. **（可选）添加到 PATH**
   ```bash
   # Linux/macOS
   echo 'alias nya="python /path/to/nya.py"' >> ~/.bashrc
   source ~/.bashrc
   
   # Windows (PowerShell)
   # 将 nya.py 所在目录添加到系统 PATH 环境变量
   ```

## ✨ 语言特性

- ✅ **图灵完备** - 完整实现 Brainfuck 的所有功能
- ✅ **猫咪友好** - 使用可爱的猫叫声作为关键字
- ✅ **大小写不敏感** - `MEOW` 和 `meow` 都可以
- ✅ **容错性强** - 自动忽略无效词汇
- ✅ **代码格式化** - 自动缩进，让代码更易读
- ✅ **双向转换** - Nya ⇄ Brainfuck 互相转换
- ✅ **交互式REPL** - 实时执行和调试
- ✅ **括号验证** - 自动检查循环结构
- ✅ **30000个内存单元** - 充足的内存空间

## 📝 语法说明

### 关键字映射表

| Nya关键字 | Brainfuck | 功能描述 | 助记 |
|----------|-----------|----------|------|
| `meow`   | `[`       | 开始循环（如果当前单元格为0，跳到对应的meom） | 猫咪开始叫 |
| `miao`   | `>`       | 指针右移 | 喵~向右走 |
| `nya`    | `<`       | 指针左移 | 喵~向左走 |
| `yaong`  | `.`       | 输出当前单元格的ASCII字符 | 大声喵叫！ |
| `miaou`  | `+`       | 当前单元格值加1 | 开心地叫 |
| `miau`   | `-`       | 当前单元格值减1 | 伤心地叫 |
| `miyav`  | `,`       | 读取输入到当前单元格 | 询问地叫 |
| `meom`   | `]`       | 结束循环（如果当前单元格非0，跳回对应的meow） | 猫咪停止叫 |

### 内存模型

```
内存: [0][0][0][0][0]...[0] (30000个单元格)
        ^
      指针
```

每个内存单元格可以存储 0-255 的值（8位无符号整数）。

## 💻 使用方法

### 命令行界面

#### 1. 交互式REPL模式
```bash
python nya.py
Nya~ Welcome to Nya REPL! (=^･ω･^=)
Type 'help' for commands, 'exit' to quit
>>> miaou miaou miaou yaong
♥
>>>
```

#### 2. 从文件运行
```bash
python nya.py filename.nya [input]

# 示例
python nya.py examples/hello_world.nya
python nya.py examples/echo.nya "Hello Nya!"
```

#### 3. 直接执行代码
```bash
python nya.py -c "nya代码" [input]

# 示例
python nya.py -c "miaou miaou miaou miaou miaou yaong"
```

#### 4. Brainfuck转Nya
```bash
python nya.py -t "brainfuck代码"

# 示例
python nya.py -t "+++++."
# 输出: miaou miaou miaou miaou miaou yaong
```

#### 5. 格式化代码
```bash
python nya.py -f filename.nya

# 示例
python nya.py -f examples/hello_world.nya
```

### REPL命令

| 命令 | 功能 |
|------|------|
| `help` | 显示帮助信息 |
| `keywords` | 显示所有Nya关键字 |
| `history` | 显示命令历史 |
| `bf <code>` | 将Brainfuck代码转换为Nya |
| `clear` | 清空内存 |
| `exit` | 退出REPL |

## 🎯 示例程序

### 1. Hello World
```nya
# 经典的Hello World程序
miaou miaou miaou miaou miaou miaou miaou miaou
meow
  miao miaou miaou miaou miaou
  meow
    miao miaou miaou
    miao miaou miaou miaou
    miao miaou miaou miaou
    miao miaou
    nya nya nya nya miau
  meom
  miao miaou
  miao miaou
  miao miau
  miao miao miaou
  meow nya meom
  nya miau
meom
miao miao yaong                    # H
miao miau miau miau yaong          # e
miaou miaou miaou miaou miaou miaou miaou yaong yaong  # ll
miaou miaou miaou yaong            # o
miao miao yaong                    # (space)
nya miau yaong                     # W
nya yaong                          # o
miaou miaou miaou yaong            # r
miau miau miau miau miau miau yaong # l
miau miau miau miau miau miau miau miau yaong # d
miao miao miaou yaong              # !
```

### 2. Echo（回显输入）
```nya
# 读取输入并输出，直到遇到NULL(0)
miyav
meow
  yaong
  miyav
meom
```

### 3. 两数相加
```nya
# 读取两个单字符数字并输出它们的和
miyav          # 读取第一个数字
miao           # 移到下一个单元格
miyav          # 读取第二个数字
nya            # 回到第一个单元格
meow           # 开始循环
  miao miaou   # 第二个单元格加1
  nya miau     # 第一个单元格减1
meom           # 结束循环
miao           # 移到结果
yaong          # 输出结果
```

### 4. 猫咪说Meow!
```nya
# 输出 "Meow!"
miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou
meow
  miao miaou miaou miaou miaou miaou miaou miaou
  miao miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou
  nya nya miau
meom
miao miaou miaou miaou miaou miaou miaou miaou yaong  # M
miao miaou yaong                                       # e
miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou yaong  # o
miau miau miau miau miau miau miau miau miau miau miau miau miau miau miau yaong                  # w
miaou miaou miaou miaou miaou miaou miaou miaou miaou miaou
meow 
  miao miaou miaou miaou
  nya miau  
meom
miao yaong                                             # !
```

### 更多示例

在 `examples/` 目录下可以找到更多示例程序：
- `hello_world.nya` - 完整的Hello World
- `echo.nya` - 输入回显程序
- `add_numbers.nya` - 简单加法计算器
- `cat_says_meow.nya` - 猫咪说话程序

## 📚 API文档

### 作为Python模块使用

```python
from nya import NyaInterpreter

# 创建解释器实例
interpreter = NyaInterpreter()

# 执行nya代码
nya_code = "miaou miaou miaou miaou miaou yaong"
result = interpreter.run(nya_code)
print(result)  # 输出: chr(5)

# 提供输入
nya_code_with_input = "miyav yaong"
result = interpreter.run(nya_code_with_input, input_data="A")
print(result)  # 输出: A

# nya与Brainfuck互转
bf_code = interpreter.nya_to_brainfuck(nya_code)
print(bf_code)  # 输出: +++++.

nya_code_back = interpreter.brainfuck_to_nya(bf_code)
print(nya_code_back)  # 输出: miaou miaou miaou miaou miaou yaong

# 验证代码语法
valid, message = interpreter.validate_brackets(nya_code)
if valid:
    print("代码语法正确！")
else:
    print(f"语法错误: {message}")

# 格式化nya代码
formatted = interpreter.format_nya_code(nya_code)
print(formatted)

# 获取执行状态
interpreter.reset()  # 重置内存和指针
memory = interpreter.memory  # 访问内存数组
pointer = interpreter.pointer  # 获取当前指针位置
```

### NyaInterpreter 类方法

| 方法 | 描述 | 参数 | 返回值 |
|------|------|------|--------|
| `run(code, input_data="")` | 执行Nya代码 | code: Nya代码字符串<br>input_data: 输入数据 | 输出字符串 |
| `nya_to_brainfuck(code)` | Nya转Brainfuck | code: Nya代码字符串 | Brainfuck代码 |
| `brainfuck_to_nya(code)` | Brainfuck转Nya | code: Brainfuck代码字符串 | Nya代码 |
| `validate_brackets(code)` | 验证括号匹配 | code: Nya代码字符串 | (bool, str) 元组 |
| `format_nya_code(code)` | 格式化代码 | code: Nya代码字符串 | 格式化后的代码 |
| `reset()` | 重置解释器状态 | 无 | 无 |
| `tokenize(code)` | 分词 | code: Nya代码字符串 | token列表 |

### 属性

| 属性 | 类型 | 描述 |
|------|------|------|
| `memory` | list | 30000个单元格的内存数组 |
| `pointer` | int | 当前内存指针位置 |
| `output` | str | 累积的输出字符串 |

## 🧪 测试

### 运行测试

```bash
# 运行Nya语言测试
python test_nya.py

# 运行Brainfuck解释器测试
python test_brainfuck.py

# 运行所有测试（使用unittest）
python -m unittest discover
```

### 测试覆盖

测试套件包含以下测试：
- ✅ 基本语法测试
- ✅ 循环结构测试
- ✅ 内存操作测试
- ✅ 输入输出测试
- ✅ 括号匹配验证
- ✅ 代码格式化测试
- ✅ Nya/Brainfuck互转测试
- ✅ 边界条件测试

## ❓ FAQ

### Q: Nya语言是图灵完备的吗？
A: 是的！Nya完整实现了Brainfuck的所有功能，因此是图灵完备的。

### Q: 可以用Nya写实际的程序吗？
A: 理论上可以，但不建议。Nya主要用于教育和娱乐目的。

### Q: 如何调试Nya程序？
A: 使用REPL模式可以逐步执行代码，或者添加yaong指令输出中间结果。

### Q: 内存限制是多少？
A: 默认30000个单元格，每个单元格存储0-255的值。

### Q: 支持注释吗？
A: 任何不是8个关键字的内容都会被忽略，可以作为注释使用。

### Q: 可以嵌套循环吗？
A: 可以！支持任意深度的循环嵌套。

### Q: 如何输入EOF？
A: 在REPL中按Ctrl+D（Linux/Mac）或Ctrl+Z（Windows）。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢 Urban Müller 创造了 Brainfuck
- 感谢所有喜欢猫咪的程序员
- 特别感谢测试和反馈的朋友们

## 📮 联系方式

- 邮箱: gouchengouceq@163.com

---

<div align="center">
  
  **用猫咪的语言编程，让世界更美好！**
  
  *Nya~ Nya~ (=^･ω･^=)*

</div>