import pypandoc
import os

# Markdown content
md_content = """
# This is a Markdown document

## Subtitle
This is a paragraph with **bold** text and *italic* text.

This is a list:
* Item 1
* Item 2

> This is a blockquote.

This is a code block:

```python
def hello_world():
    print("Hello, world!")
```

This is a link to [Google](https://www.google.com).
"""

# output_path = "/mnt/data/proof.md"
output_path = "/data/proof.md"

# Validate output path
if not os.path.exists(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

pypandoc.convert_text(md_content, 'md', format='md', outputfile=output_path, extra_args=['--standalone'])

output_path