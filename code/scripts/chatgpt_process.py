#!/usr/bin/env python3
import re
import sys
import os

def convert_math(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0

    # ((...))
    double_re = re.compile(r"\(\(([^()]*)\)\)")
    # (x) 但不匹配 ((...))
    single_re = re.compile(r"(?<!\()\( ([^()]+) \)(?!\))".replace(" ", ""))

    while i < len(lines):
        line = lines[i]

        # ---------- 数学块 [ ... ] ----------
        if line.strip() == "[":
            out.append("$$")
            i += 1
            while i < len(lines) and lines[i].strip() != "]":
                out.append(lines[i])   # 数学块内保持原样
                i += 1
            out.append("$$")
            i += 1  # 跳过 "]"
            continue

        # ---------- 行内：((...)) 和 (...) ----------
        line = double_re.sub(r"$(\1)$", line)
        line = single_re.sub(r"$\1$", line)

        out.append(line)
        i += 1

    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print("用法: python convert.py 输入文件")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"文件不存在: {filename}")
        sys.exit(1)

    # 读取原文件
    with open(filename, "r", encoding="utf-8") as f:
        original = f.read()

    # 转换
    converted = convert_math(original)

    # 覆盖写回
    with open(filename, "w", encoding="utf-8") as f:
        f.write(converted)

    print(f"已原地处理: {filename}")


if __name__ == "__main__":
    main()
