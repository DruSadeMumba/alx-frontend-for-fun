def parse_listing(md_text):
    """Parse listing"""
    html_text = ""
    for line in md_text.split("\n"):
        if line.startswith("-"):
            html_text += "<ul>\n"
            texts = line.split("-")
            for text in texts[1:]:
                if text.strip():
                    html_text += f"<li>{text.strip()}</li>\n"
            html_text += "</ul>\n"
        elif line.startswith("*"):
            html_text += "<ol>\n"
            texts = line.split("*")
            for text in texts[1:]:
                if text.strip():
                    html_text += f"\t<li>{text.strip()}</li>\n"
            html_text += "</ol>\n"
        else:
            html_text += f"{ line}\n"
    return html_text
