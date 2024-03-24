#!/usr/bin/python3
"""Markdown to HTML"""
import sys


def parse_headings(md_text):
    """Parse headings"""
    html_text = ""
    for line in md_text.split('\n'):
        if line.startswith("#"):
            level = line.count("#")
            text = line[level:].strip()
            html_text += f"<h{level}>{text}</h{level}>\n"
        else:
            html_text += f"{line}"
    return html_text


def parse_unordered_list(md_text):
    """Parse unordered listing"""
    html_text = ""
    for line in md_text.split("\n"):
        if line.startswith("-"):
            html_text += f"<ul>\n"
            text = line[1:].strip()
            for ln in text.split("-"):
                html_text += f"<li>{ln}</li>\n"
            html_text += f"</ul>\n"
        else:
            html_text += f"{line}\n"
    return html_text


def parse_ordered_list(md_text):
    """Parse unordered listing"""
    html_text = ""
    for line in md_text.split("\n"):
        if line.startswith("*"):
            html_text += f"<ol>\n"
            text = line[1:].strip()
            for ln in text.split("*"):
                html_text += f"\t<li>{ln}</li>\n"
            html_text += f"</ol>\n"
        else:
            html_text += f"{line}\n"
    return html_text


def parse_md(md_text):
    """Parse Markdown text"""
    html_text = parse_headings(md_text)
    html_text = parse_unordered_list(html_text)
    html_text = parse_ordered_list(html_text)
    return html_text


def markdown2html(md_file, html_file):
    """Convert md file to html file"""
    try:
        with open(md_file, 'r') as f:
            md_text = f.read()
            html_text = parse_md(md_text)
            with open(html_file, 'w') as out_f:
                out_f.write(html_text)
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
