# jmd - Jupyter to Markdown

**Complete** Jupyter notebook to markdown converter.

## The Problem

`jupyter nbconvert --to markdown` silently drops code cells that don't have outputs. This breaks:
- Documentation from Colab notebooks
- Code review workflows
- Version control diffs
- Archival and reference materials

## The Solution

`jmd` converts notebooks to markdown **without dropping any cells**.

## Installation

```bash
# TODO: Add installation instructions
```

## Usage

```bash
# Convert a single notebook
python jmd.py notebook.ipynb

# Specify output filename
python jmd.py notebook.ipynb -o output.md

# Convert multiple notebooks
python jmd.py *.ipynb
```

## Features

- ✅ Preserves ALL cells (code and markdown)
- ✅ Includes code cells without outputs
- ✅ Formats outputs correctly (stdout, results, errors)
- ✅ Fast and simple (stdlib only)
- ✅ Clear conversion feedback

## Output Format

```markdown
## Cell 1 (code) [1]
```python
print("Hello, world!")
```

**Output:**
```
Hello, world!
```

---

## Cell 2 (code) [not executed]
```python
x = 42
```

---
```

## Requirements

- Python 3.8+
- No external dependencies (stdlib only)

## Project Status

Created: 2025-11-12
Status: 🚧 In Development

## License

TODO: Add license
