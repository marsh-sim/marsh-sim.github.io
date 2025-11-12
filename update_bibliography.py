#!/usr/bin/env python3

"""
Updates the bibliography page from BibTeX file.
Doesn't accept configuration arguments by design.
"""

from datetime import datetime
from io import StringIO
from mistune import create_markdown, BlockState
from mistune.renderers.markdown import MarkdownRenderer
from os import path as p
from pybtex.backends.markdown import Backend
from pybtex.database import BibliographyData, parse_file
from pybtex.style.formatting.unsrt import Style

# allow running from anywhere
root_p = p.dirname(__file__)

bib_path = p.join(root_p, "docs", "bibliography.bib")
bib_entries = parse_file(bib_path).entries
bib_parts = {}
with open(bib_path, "r") as bib_file:
    content = bib_file.read()
    for part in content.split("@"):
        part = part.strip()
        if len(part) == 0:
            continue
        part = "@" + part
        start = part.index("{") + 1
        end = part.index(",")
        key = part[start:end]
        bib_parts[key] = part

md_path = p.join(root_p, "docs", "bibliography.md")
md_ast = []
with open(md_path, "r") as md_file:
    md_ast = create_markdown(renderer=None)(md_file.read())

# iterate from end so indices don't change
for i in range(len(md_ast)-1, -1, -1):
    block = md_ast[i]
    if not (block["type"] == "heading" and "children" in block and len(block["children"]) == 1):
        continue

    child = block["children"][0]
    if not (child["type"] == "text"):
        continue

    key = child["raw"]
    if not key in bib_entries:
        continue

    next_paragraph_index = None
    j = i + 1
    while j < len(md_ast):
        candidate = md_ast[j]
        if candidate["type"] == "blank_line":
            j += 1
            continue
        if candidate["type"] == "block_html":
            # remove the details block
            del md_ast[j]
            continue

        if candidate["type"] == "paragraph":
            next_paragraph_index = j
            break
        else:
            break
        
    if next_paragraph_index is None:
        md_ast.insert(i + 1, {
            "type": "paragraph",
            "children": [{"raw": "lorem ipsum", "type": "text"}]
        })
        next_paragraph_index = i + 1
        print("insert for", key)
    else:
        print("replace for", key)

    single_data = BibliographyData()
    single_data.add_entry(key, bib_entries[key])
    formatted = Style().format_bibliography(single_data)
    stream = StringIO()
    Backend().write_to_stream(formatted, stream)
    md_ast[next_paragraph_index]["children"] = [{
        "raw": f"""
<details>
<summary>Show BibTeX</summary>
```bibtex
{bib_parts[key]}
```
</details>

{stream.getvalue()[4:]}
""".strip(),
        "type": "text"
    }]

with open(md_path, "w") as md_file:
    md_file.write(MarkdownRenderer()(md_ast, BlockState()))
