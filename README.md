# Nya Language 🐱

Nya是一门基于Brainfuck的猫咪友好编程语言，使用猫叫声作为关键字。

## 语言映射

| Nya关键字 | Brainfuck | 功能描述 |
|----------|-----------|----------|
| `meow`   | `[`       | 开始循环（如果当前单元格为0，跳到对应的meom） |
| `miao`   | `>`       | 指针右移 |
| `nya`    | `<`       | 指针左移 |
| `yaong`  | `.`       | 输出当前单元格的ASCII字符 |
| `miaou`  | `+`       | 当前单元格值加1 |
| `miau`   | `-`       | 当前单元格值减1 |
| `miyav`  | `,`       | 读取输入到当前单元格 |
| `meom`   | `]`       | 结束循环（如果当前单元格非0，跳回对应的meow） |

## 安装与使用

### 命令行使用

#### 交互式REPL模式
```bash
python nya.py
```
进入交互式环境，可以实时执行nya代码。

#### 从文件运行
```bash
python nya.py filename.nya [input]
```

#### 直接运行代码
```bash
python nya.py -c "nya代码" [input]
```

#### Brainfuck转Nya
```bash
python nya.py -t "brainfuck代码"
```

#### 格式化nya代码
```bash
python nya.py -f filename.nya
```

### 示例程序

#### Hello World
```nya
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
miao miao yaong
miao miau miau miau yaong
miaou miaou miaou miaou miaou miaou miaou yaong yaong
miaou miaou miaou yaong
miao miao yaong
nya miau yaong
nya yaong
miaou miaou miaou yaong
miau miau miau miau miau miau yaong
miau miau miau miau miau miau miau miau yaong
miao miao miaou yaong
miao miaou miaou yaong
```

#### Echo（回显输入）
```nya
miyav
meow
  yaong
  miyav
meom
```

#### 加法
```nya
miyav
miao
miyav
nya
meow
  miao miaou
  nya miau
meom
miao
yaong
```

### 作为Python模块使用

```python
from nya import NyaInterpreter

# 创建解释器实例
interpreter = NyaInterpreter()

# 执行nya代码
nya_code = "miaou miaou miaou miaou miaou yaong"
result = interpreter.run(nya_code)
print(result)  # 输出: chr(5)

# nya与Brainfuck互转
bf_code = interpreter.nya_to_brainfuck(nya_code)
nya_code_back = interpreter.brainfuck_to_nya(bf_code)

# 验证代码语法
valid, message = interpreter.validate_brackets(nya_code)

# 格式化nya代码
formatted = interpreter.format_nya_code(nya_code)
```

## REPL命令

在交互式模式下，支持以下命令：

- `help` - 显示帮助信息
- `keywords` - 显示nya语言关键字
- `history` - 显示命令历史
- `bf <code>` - 将Brainfuck代码转换为Nya
- `exit` - 退出REPL

## 特性

- ✅ 完整实现Brainfuck的图灵完备性
- ✅ 大小写不敏感（MEOW和meow都可以）
- ✅ 忽略无效的词汇（只识别8个猫叫关键字）
- ✅ 括号匹配验证
- ✅ 代码格式化功能
- ✅ 双向转换（Nya ⇄ Brainfuck）
- ✅ 交互式REPL环境
- ✅ 30000个内存单元

## 测试

运行测试套件：
```bash
python test_nya.py
```

## 依赖

- Python 3.6+
- brainfuck.py（Brainfuck解释器）

## 许可

MIT License

---
*Nya~ Nya~ (=^･ω･^=)*