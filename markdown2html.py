#!/usr/bin/python3
"""Markdown to HTML"""
import sys
import markdown


def markdown2html(md_file, html_file):
    """Convert md file to html file"""
    try:
        with open(md_file, 'r') as f:
            f.read()
            if md_file and html_file:
                sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    else:
        markdown2html(sys.argv[1], sys.argv[2])
        sys.exit(0)
