#!/usr/bin/python3
'''
Script to render markdown in html
'''
import sys
from os import path
import re


# Patterns
headings_pattern = r'^#{1,6}\s*'
unordered_pattern = r'^-\s*'
ordered_pattern = r'^\*\s*'
bold_pattern = r'\*\*(.*?)\*\*'
italic_pattern = r'__(.*?)__'


def main():
    args = sys.argv

    lines = []
    is_ul = False
    is_ol = False
    is_p = False

    if len(args) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    markdown_path = args[1]
    html_path = args[2]

    if not path.exists(markdown_path):
        print(f"Missing {markdown_path}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_path, mode='r') as markdown:
        for line in markdown:
            # Markdown Headings
            if re.match(headings_pattern, line):
                lines.append(handle_heading(line.strip()))
                continue

            # Markdown Unordered List
            if re.match(unordered_pattern, line):
                line = re.sub(unordered_pattern, '', line.strip())
                if not is_ul:
                    is_ul = True
                    lines.append('<ul>\n')

                lines.append(f'<li>{handle_bold_italic(line)}</li>\n')
                continue

            # Markdown Ordered List
            if re.match(ordered_pattern, line):
                line = re.sub(ordered_pattern, '', line.strip())
                if not is_ol:
                    is_ol = True
                    lines.append('<ol>\n')

                lines.append(f'<li>{handle_bold_italic(line)}</li>\n')
                continue

            # Markdown paragraph
            if line.strip():
                if is_p:
                    lines.append('<br/>\n')
                    lines.append(handle_bold_italic(line.strip()) + '\n')
                else:
                    lines.append('<p>\n')
                    lines.append(handle_bold_italic(line.strip()) + '\n')
                    is_p = True
                continue

            if is_p:
                lines.append('</p>\n')
                is_p = False
            if is_ul:
                lines.append('</ul>\n')
                is_ul = False
            if is_ol:
                lines.append('</ol>\n')
                is_ol = False

        if is_p:
            lines.append('</p>\n')
            is_p = False
        if is_ul:
            lines.append('</ul>\n')
            is_ul = False
        if is_ol:
            lines.append('</ol>\n')
            is_ol = False

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


def handle_bold_italic(text):
    text = re.sub(bold_pattern, r'<b>\1</b>', text)
    text = re.sub(italic_pattern, r'<em>\1</em>', text)
    return text

if __name__ == '__main__':
    main()
