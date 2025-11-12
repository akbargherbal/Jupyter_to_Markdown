"""
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
