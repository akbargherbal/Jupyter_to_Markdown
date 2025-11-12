import json
import sys
from pathlib import Path
from argparse import ArgumentParser

def format_markdown_cell(cell, cell_num):
    """Formats a markdown cell."""
    source = ''.join(cell['source'])
    return f"## Cell {cell_num} (markdown)\n\n{source}\n\n---\n"

def format_code_cell(cell, cell_num):
    """Formats a code cell's source code."""
    source = ''.join(cell['source'])
    # Use a space for execution_count if it's null, as per notebook format
    exec_count = cell.get('execution_count') or ' '

    # Determine if the cell has output to add a note
    no_output_note = ""
    if not cell.get('outputs'):
        no_output_note = " [no output]"

    header = f"## Cell {cell_num} (code){no_output_note} [{exec_count}]"
    code_block = f"```python\n{source}\n```"
    
    return f"{header}\n\n{code_block}\n\n"

def format_output(output):
    """Formats a single output block from a code cell."""
    output_type = output.get('output_type', 'unknown')

    if output_type == 'stream':
        # stdout/stderr
        text = ''.join(output.get('text', ''))
        return f"**Output (stream):**\n```text\n{text.strip()}\n```\n\n"

    elif output_type == 'execute_result':
        # The return value of a cell
        data = output.get('data', {})
        if 'text/plain' in data:
            text = ''.join(data['text/plain'])
            return f"**Result:**\n```text\n{text.strip()}\n```\n\n"

    elif output_type == 'error':
        # Exceptions and tracebacks
        traceback = '\n'.join(output.get('traceback', []))
        return f"**Error:**\n```ansi\n{traceback}\n```\n\n"
        
    elif output_type == 'display_data':
        # Richer outputs like images or plots
        data = output.get('data', {})
        if 'text/plain' in data:
            text = ''.join(data['text/plain'])
            return f"**Display Data:**\n```text\n{text.strip()}\n```\n\n"

    return ""  # Return empty string for unsupported or empty output types

def convert_notebook(ipynb_path, output_path=None):
    """
    Converts a Jupyter Notebook (.ipynb) to a complete Markdown file,
    ensuring no cells are dropped.
    """
    # 1. Load notebook
    notebook_path = Path(ipynb_path)
    with notebook_path.open('r', encoding='utf-8') as f:
        nb = json.load(f)

    # 2. Prepare output path
    if output_path:
        output_file = Path(output_path)
    else:
        output_file = notebook_path.with_suffix('.md')
    
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # 3. Convert all cells
    markdown_content = []
    cells_with_outputs = 0
    total_cells = len(nb.get('cells', []))

    for i, cell in enumerate(nb.get('cells', []), 1):
        cell_type = cell.get('cell_type')
        if cell_type == 'markdown':
            markdown_content.append(format_markdown_cell(cell, i))
        elif cell_type == 'code':
            markdown_content.append(format_code_cell(cell, i))
            
            if cell.get('outputs'):
                cells_with_outputs += 1
                for output in cell['outputs']:
                    markdown_content.append(format_output(output))

    # 4. Write to file
    output_text = ''.join(markdown_content)
    output_file.write_text(output_text, encoding='utf-8')

    # 5. Return stats for summary
    return {
        'total_cells': total_cells,
        'cells_with_outputs': cells_with_outputs,
        'output_path': str(output_file)
    }

def main():
    """CLI entry point."""
    parser = ArgumentParser(description='Convert Jupyter notebooks to complete markdown without dropping cells.')
    parser.add_argument('notebook_path', help='Path to the input .ipynb notebook file.')
    parser.add_argument('-o', '--output', help='Path for the output .md file. If not provided, it will be saved next to the notebook.')
    
    args = parser.parse_args()

    try:
        stats = convert_notebook(args.notebook_path, args.output)
        code_only_cells = stats['total_cells'] - stats['cells_with_outputs']
        print(f"✓ Conversion successful!")
        print(f"  - Total cells processed: {stats['total_cells']}")
        print(f"  - Cells with outputs:  {stats['cells_with_outputs']}")
        print(f"  - Code-only cells:     {code_only_cells}")
        print(f"✓ Output saved to: {stats['output_path']}")
    except FileNotFoundError:
        print(f"✗ Error: Input file not found at '{args.notebook_path}'", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"✗ Error: Could not parse the notebook file. It might be corrupted.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
