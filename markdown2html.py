#!/usr/bin/python3
'''
Script to render markdown in html
'''
import sys
from os import path


def main():
    args = sys.argv

    if len(args) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    markdown = args[1]
    # html = args[2]

    if not path.exists(markdown):
        print(f"Missing {markdown}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
