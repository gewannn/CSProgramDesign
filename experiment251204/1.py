from keyword import iskeyword
from tokenize import generate_tokens, untokenize, NAME, TokenInfo
from io import StringIO
import os
#  增加关键词防止被转化成大写
SKIP_NAMES = {
    "input", "print", "eval", "len", "range", "int",
    "float", "str", "list", "dict", "tuple", "set",
    "open", "type", "bool"
}
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
def process_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        src = f.read()
def upper_code(src: str) -> str:
    new_tokens = []

    for t in generate_tokens(StringIO(src).readline):
        if (
            t.type == NAME
            and t.string.islower()
            and not iskeyword(t.string)
            and t.string not in SKIP_NAMES
        ):
            t = TokenInfo(t.type, t.string.upper(), t.start, t.end, t.line)
        new_tokens.append(t)
    new_src = untokenize(new_tokens)
    return new_src
def process_file(filename: str):
    """读取文件 -> 转换 -> 写新文件"""
    with open(filename, "r", encoding="utf-8") as f:
        src = f.read()
    new_src = upper_code(src)
    base, ext = os.path.splitext(filename)
    new_filename = base + "_UPPER" + ext
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(new_src)
    print("转换完成，新文件为：", new_filename)
if __name__ == "__main__":
    name = input("请输入要处理的 .py 文件名：")
    process_file(name)