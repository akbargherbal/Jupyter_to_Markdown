"""
scaffold.py - Project Structure Generator

Creates the complete directory structure and placeholder files for the jmd project.
Usage: python scaffold.py [--path <target_directory>]
"""

import sys
from pathlib import Path
from datetime import datetime
from argparse import ArgumentParser


def create_file(path: Path, content: str):
    """Create a file with the given content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    print(f"  ✓ Created: {path}")


def scaffold_jmd_project(base_path: Path):
    """Create the complete jmd project structure."""
    
    print(f"\n🏗️  Scaffolding jmd project at: {base_path}\n")
    
    # Create base directory
    base_path.mkdir(parents=True, exist_ok=True)
    
    # ==========================================
    # Main converter script
    # ==========================================
    jmd_script = '''"""
jmd.py - Jupyter to Markdown Converter

Converts Jupyter notebooks (.ipynb) to complete markdown files.
Unlike jupyter nbconvert, this preserves ALL cells including code cells without outputs.

Usage:
    python jmd.py notebook.ipynb
    python jmd.py notebook.ipynb -o output.md
    python jmd.py *.ipynb
"""

import json
import sys
from pathlib import Path
from argparse import ArgumentParser


def load_notebook(path):
    """Load and parse a Jupyter notebook file."""
    # TODO: Implement notebook loading
    pass


def format_markdown_cell(cell, cell_num):
    """Format a markdown cell."""
    # TODO: Implement markdown cell formatting
    pass


def format_code_cell(cell, cell_num):
    """Format a code cell with syntax highlighting."""
    # TODO: Implement code cell formatting
    pass


def format_output(output):
    """Format different types of cell outputs."""
    # TODO: Handle output types:
    # - stream (stdout/stderr)
    # - execute_result (return values)
    # - display_data (plots, images)
    # - error (exceptions, tracebacks)
    pass


def convert_notebook(ipynb_path, output_path=None):
    """
    Convert a Jupyter notebook to markdown.
    
    Args:
        ipynb_path: Path to .ipynb file
        output_path: Optional output path (defaults to same name with .md)
    
    Returns:
        dict: Conversion statistics
    """
    # TODO: Main conversion logic
    pass


def main():
    """CLI entry point."""
    parser = ArgumentParser(
        description='Convert Jupyter notebooks to complete markdown (preserves all cells)'
    )
    parser.add_argument('notebook', nargs='+', help='Path to .ipynb file(s)')
    parser.add_argument('-o', '--output', help='Output markdown file path')
    parser.add_argument('--verbose', action='store_true', help='Show detailed output')
    
    args = parser.parse_args()
    
    # TODO: Process notebooks and handle errors
    pass


if __name__ == '__main__':
    main()
'''
    
    create_file(base_path / 'jmd.py', jmd_script)
    
    # ==========================================
    # README
    # ==========================================
    readme = f'''# jmd - Jupyter to Markdown

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

Created: {datetime.now().strftime('%Y-%m-%d')}
Status: 🚧 In Development

## License

TODO: Add license
'''
    
    create_file(base_path / 'README.md', readme)
    
    # ==========================================
    # Test directory and files
    # ==========================================
    test_readme = '''# Test Cases

## Test Notebooks

- `test_all_outputs.ipynb` - Every cell has output
- `test_no_outputs.ipynb` - No cells have outputs
- `test_mixed.ipynb` - Mix of markdown, code, outputs
- `test_empty.ipynb` - Empty notebook
- `test_errors.ipynb` - Cells with error outputs

## Running Tests

```bash
# TODO: Add test running instructions
python -m pytest tests/
```

## Adding Test Cases

1. Create notebook in `test_notebooks/`
2. Add expected output in `expected_outputs/`
3. Add test in `test_jmd.py`
'''
    
    create_file(base_path / 'tests' / 'README.md', test_readme)
    
    # Test script
    test_script = '''"""
test_jmd.py - Test suite for jmd converter

Run with: pytest tests/test_jmd.py
"""

import pytest
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import jmd


def test_load_notebook():
    """Test notebook loading."""
    # TODO: Implement test
    pass


def test_format_markdown_cell():
    """Test markdown cell formatting."""
    # TODO: Implement test
    pass


def test_format_code_cell():
    """Test code cell formatting."""
    # TODO: Implement test
    pass


def test_format_output_stream():
    """Test stdout/stderr output formatting."""
    # TODO: Implement test
    pass


def test_format_output_result():
    """Test execute_result formatting."""
    # TODO: Implement test
    pass


def test_format_output_error():
    """Test error/traceback formatting."""
    # TODO: Implement test
    pass


def test_convert_notebook_all_outputs():
    """Test conversion of notebook where all cells have outputs."""
    # TODO: Implement test
    pass


def test_convert_notebook_no_outputs():
    """Test conversion of notebook where no cells have outputs."""
    # TODO: Implement test
    pass


def test_convert_notebook_mixed():
    """Test conversion of mixed markdown/code notebook."""
    # TODO: Implement test
    pass


def test_cell_count_preservation():
    """Ensure no cells are dropped during conversion."""
    # TODO: Implement test - this is the critical test!
    pass
'''
    
    create_file(base_path / 'tests' / 'test_jmd.py', test_script)
    
    # Placeholder for test notebooks directory
    test_notebooks_readme = '''# Test Notebooks

Place test `.ipynb` files here.

These will be used to verify jmd works correctly across different notebook types.
'''
    
    create_file(base_path / 'tests' / 'test_notebooks' / 'README.md', test_notebooks_readme)
    
    # Placeholder for expected outputs
    expected_readme = '''# Expected Outputs

Expected markdown outputs for test notebooks.

Used to verify jmd produces correct results.
'''
    
    create_file(base_path / 'tests' / 'expected_outputs' / 'README.md', expected_readme)
    
    # ==========================================
    # Documentation
    # ==========================================
    usage_doc = '''# Usage Guide

## Basic Usage

### Convert Single Notebook

```bash
python jmd.py notebook.ipynb
```

Creates `notebook.md` in the same directory.

### Specify Output File

```bash
python jmd.py notebook.ipynb -o output.md
```

### Convert Multiple Notebooks

```bash
python jmd.py notebook1.ipynb notebook2.ipynb notebook3.ipynb
```

## Output Format

TODO: Document the markdown output format

## PowerShell Alias Setup

TODO: Document PowerShell alias configuration

## Common Use Cases

### Documenting Colab Notebooks

TODO: Add workflow example

### Code Review

TODO: Add workflow example

### Version Control

TODO: Add workflow example
'''
    
    create_file(base_path / 'docs' / 'USAGE.md', usage_doc)
    
    # Development guide
    dev_doc = '''# Development Guide

## Project Structure

```
jmd/
├── jmd.py                 # Main converter script
├── README.md              # Project documentation
├── tests/                 # Test suite
│   ├── test_jmd.py       # Test cases
│   ├── test_notebooks/   # Test input files
│   └── expected_outputs/ # Expected results
└── docs/                  # Documentation
    ├── USAGE.md          # Usage guide
    └── DEVELOPMENT.md    # This file
```

## Development Setup

TODO: Add setup instructions

## Running Tests

TODO: Add test running instructions

## Adding Features

TODO: Add contribution guidelines

## Code Style

- Follow PEP 8
- Use type hints where helpful
- Keep functions focused and testable
- Document edge cases
'''
    
    create_file(base_path / 'docs' / 'DEVELOPMENT.md', dev_doc)
    
    # ==========================================
    # Configuration files
    # ==========================================
    
    # .gitignore
    gitignore = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# Testing
.pytest_cache/
.coverage
htmlcov/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Test outputs
tests/output/
*.md
!README.md
!docs/**/*.md

# Notebooks
*.ipynb_checkpoints/
'''
    
    create_file(base_path / '.gitignore', gitignore)
    
    # Requirements (even though we don't need them, good to have structure)
    requirements = '''# No external dependencies required for core functionality
# jmd uses only Python stdlib

# Optional: for development/testing
pytest>=7.0.0
'''
    
    create_file(base_path / 'requirements.txt', requirements)
    
    # ==========================================
    # Output directory for test runs
    # ==========================================
    output_readme = '''# Output Directory

This directory is for testing jmd output during development.

Files here are gitignored - this is just a workspace.
'''
    
    create_file(base_path / 'output' / 'README.md', output_readme)
    
    # ==========================================
    # Summary
    # ==========================================
    print("\n" + "="*50)
    print("✅ Project scaffolding complete!")
    print("="*50)
    print(f"\nProject created at: {base_path.resolve()}")
    print("\nDirectory structure:")
    print(f"""
jmd/
├── jmd.py                      # Main converter script
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies (none needed!)
├── .gitignore                  # Git ignore rules
├── tests/
│   ├── test_jmd.py            # Test suite
│   ├── test_notebooks/        # Test input files
│   └── expected_outputs/      # Expected results
├── docs/
│   ├── USAGE.md               # Usage guide
│   └── DEVELOPMENT.md         # Dev guide
└── output/                     # Test output workspace
    """)
    
    print("\n📋 Next steps:")
    print("  1. cd jmd")
    print("  2. Review jmd.py structure")
    print("  3. Implement core functions")
    print("  4. Test with problem notebook")
    print("  5. Set up PowerShell alias")
    print()


def main():
    parser = ArgumentParser(description='Scaffold the jmd project structure')
    parser.add_argument(
        '--path',
        type=Path,
        default=Path.cwd() / 'jmd',
        help='Target directory for project (default: ./jmd)'
    )
    
    args = parser.parse_args()
    
    try:
        scaffold_jmd_project(args.path)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()