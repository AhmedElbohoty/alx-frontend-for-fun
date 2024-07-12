#!/usr/bin/python3
'''
Script to render markdown in html
'''
import sys
from os import path
import re


# Patterns
headings_pattern = r'^#{1,6}\s*'


def main():
    args = sys.argv

    if len(args) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    markdown_path = args[1]
    html_path = args[2]

    if not path.exists(markdown_path):
        print(f"Missing {markdown_path}", file=sys.stderr)
        sys.exit(1)

    lines = []
    with open(markdown_path, mode='r') as markdown:
        for line in markdown:
            if re.match(headings_pattern, line):
                lines.append(handle_heading(line.strip()))

    with open(html_path, mode='w') as html:
        html.writelines(lines)

    sys.exit(0)


def handle_heading(line):
    '''
    Parsing Headings Markdown syntax for generating HTML

    Return: html tag
    '''
    if line.startswith('# '):
        line = re.sub(headings_pattern, '', line)
        return f'<h1>{line}</h1>\n'

    if line.startswith('## '):
        line = re.sub(headings_pattern, '', line)
        return f'<h2>{line}</h2>\n'

    if line.startswith('### '):
        line = re.sub(headings_pattern, '', line)
        return f'<h3>{line}</h3>\n'

    if line.startswith('#### '):
        line = re.sub(headings_pattern, '', line)
        return f'<h4>{line}</h4>\n'

    if line.startswith('##### '):
        line = re.sub(headings_pattern, '', line)
        return f'<h5>{line}</h5>\n'

    if line.startswith('###### '):
        line = re.sub(headings_pattern, '', line)
        return f'<h6>{line}</h6>\n'

    return line


if __name__ == '__main__':
    main()
