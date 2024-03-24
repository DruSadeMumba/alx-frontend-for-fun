#!/usr/bin/python3
"""Markdown to HTML"""
import sys


def parse_heading(md_text):
    """Parse heading based on starting character"""
    html_text = ""
    if md_text.startswith("#"):
        level = md_text.count("#")
        text = md_text[level:].strip()
        html_text += f"<h{level}>{text}</h{level}>\n"
    return html_text


def parse_list(md_text, list_type):
    """Parse unordered or ordered list"""
    html_text = ""
    html_text += "<ul>\n" if list_type == "-" else "<ol>\n"
    for line in md_text:
        if line.startswith(list_type):
            html_text += f"\t<li>{line[1:].strip()}</li>\n"
        else:
            break
    html_text += "</ul>\n" if list_type == "-" else "</ol>\n"
    return html_text


def parse_markdown(md_text):
    """Parse headings and lists"""
    html_text = ""
    lines = md_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            html_text += parse_heading(line)
        elif line.startswith("*") or line.startswith("-"):
            list_type = "*" if line.startswith("*") else "-"
            html_text += parse_list(lines[i:], list_type)
            i += 1
        else:
            html_text += f"{line}\n"
        i += 1
    return html_text


def markdown2html(md_file, html_file):
    """Convert md file to html file"""
    try:
        with open(md_file, 'r') as f:
            md_text = f.read()
            html_text = parse_markdown(md_text)
            with open(html_file, 'w') as out_f:
                out_f.write(html_text)
            sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    markdown2html('README.md', 'README.html')
    sys.exit(0)

