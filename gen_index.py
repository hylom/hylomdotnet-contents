#!/usr/bin/env python3

from pathlib import Path
import re
import sys

def generate_index(p, dir_stack=[], force=False):
    # generate _index.md
    index_md = p / '_index.md'
    if ((not index_md.exists() or force)
        and len(dir_stack) != 0
        and re.match(r'^\d+$', p.name)):
        with index_md.open(mode='w', encoding="utf8") as fp:
            fp.write(generate_header(index_md, dir_stack))

    # search sub directroy
    for child in p.iterdir():
        if child.name[0] == ".":
            continue
        if child.is_dir():
            stack = list(dir_stack)
            stack.append(child.name)
            generate_index(child, stack, force)


def generate_header(p, stack):
    content = ""
    if len(stack) == 1:
        content = "title: {}年".format(stack[0])
    elif len(stack) == 2:
        content = "title: {}年{}月".format(*stack[:2])
    elif len(stack) == 3:
        content = "title: {}年{}月{}日".format(*stack[:3])
    if content:
        return "---\n{}\n---\n".format(content)
    return ""
                     
def main():
    force = False
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg == "-f":
                force = True
    path = "."
    p = Path(path)
    generate_index(p, force=force)

if __name__ == '__main__':
    main()
