import sys
import pytest
import json
import subprocess
from pathlib import Path

# Make the script's functions available for testing
from jmd import (
    format_markdown_cell,
    format_code_cell,
    format_output,
    convert_notebook
)

# --- Test Data Fixtures ---

@pytest.fixture
def markdown_cell_fixture():
    return {
        "cell_type": "markdown",
        "source": ["# Hello\n", "This is a test."]
    }

@pytest.fixture
def code_cell_with_output_fixture():
    return {
        "cell_type": "code",
        "execution_count": 1,
        "source": ["print('hello world')"],
        "outputs": [{
            "name": "stdout",
            "output_type": "stream",
            "text": ["hello world\n"]
        }]
    }

@pytest.fixture
def code_cell_no_output_fixture():
    return {
        "cell_type": "code",
        "execution_count": 2,
        "source": ["x = 10"],
        "outputs": []
    }

@pytest.fixture
def error_output_fixture():
    return {
        "output_type": "error",
        "ename": "NameError",
        "evalue": "name 'x' is not defined",
        "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------",
            "NameError: name 'x' is not defined"
        ]
    }

# --- Unit Tests for Formatting Functions ---

def test_format_markdown_cell(markdown_cell_fixture):
    result = format_markdown_cell(markdown_cell_fixture, 1)
    assert "## Cell 1 (markdown)" in result
    assert "# Hello\nThis is a test." in result
    assert result.endswith("---\n")

def test_format_code_cell_with_output(code_cell_with_output_fixture):
    result = format_code_cell(code_cell_with_output_fixture, 2)
    assert "## Cell 2 (code) [1]" in result
    assert "print('hello world')" in result
    assert "[no output]" not in result

def test_format_code_cell_no_output(code_cell_no_output_fixture):
    result = format_code_cell(code_cell_no_output_fixture, 3)
    assert "## Cell 3 (code) [no output] [2]" in result
    assert "x = 10" in result

def test_format_output_stream(code_cell_with_output_fixture):
    output = code_cell_with_output_fixture['outputs'][0]
    result = format_output(output)
    assert "**Output (stream):**" in result
    assert "hello world" in result

def test_format_output_error(error_output_fixture):
    result = format_output(error_output_fixture)
    assert "**Error:**" in result
    assert "NameError: name 'x' is not defined" in result

def test_format_unsupported_output():
    output = {"output_type": "unknown_type", "data": {}}
    result = format_output(output)
    assert result == ""

# --- Integration Test for Full Conversion ---

def test_convert_notebook_integration(tmp_path):
    # tmp_path is a pytest fixture for a temporary directory
    notebook_path = tmp_path / "test.ipynb"
    output_path = tmp_path / "test.md"
    
    # Create a synthetic notebook file
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": ["Markdown cell"]},
            {"cell_type": "code", "execution_count": 1, "source": ["print('Code cell')"], "outputs": [{"output_type": "stream", "name": "stdout", "text": ["Code cell\n"]}]}
        ],
        "nbformat": 4, "nbformat_minor": 2
    }
    notebook_path.write_text(json.dumps(notebook_content))

    stats = convert_notebook(str(notebook_path), str(output_path))

    # Verify stats
    assert stats['total_cells'] == 2
    assert stats['cells_with_outputs'] == 1
    assert stats['output_path'] == str(output_path)

    # Verify output file content
    md_content = output_path.read_text()
    assert "## Cell 1 (markdown)" in md_content
    assert "Markdown cell" in md_content
    assert "## Cell 2 (code) [1]" in md_content
    assert "print('Code cell')" in md_content
    assert "**Output (stream):**" in md_content

# --- CLI Tests ---

def test_cli_success(tmp_path):
    notebook_path = tmp_path / "test.ipynb"
    notebook_path.write_text('{"cells": [], "nbformat": 4, "nbformat_minor": 2}')
    
    result = subprocess.run(
        ["python3", "jmd.py", str(notebook_path)],
        capture_output=True, text=True
    )
    
    assert result.returncode == 0
    assert "✓ Conversion successful!" in result.stdout
    assert "Output saved to:" in result.stdout

def test_cli_file_not_found():
    result = subprocess.run(
        ["python3", "jmd.py", "non_existent_file.ipynb"],
        capture_output=True, text=True
    )
    
    assert result.returncode == 1
    assert "Error: Input file not found" in result.stderr

def test_cli_corrupted_file(tmp_path):
    corrupted_file = tmp_path / "corrupted.ipynb"
    corrupted_file.write_text("this is not json")
    
    result = subprocess.run(
        ["python3", "jmd.py", str(corrupted_file)],
        capture_output=True, text=True
    )
    
    assert result.returncode == 1
    assert "Error: Could not parse the notebook file" in result.stderr

# --- New Tests to Increase Coverage ---

@pytest.fixture
def execute_result_fixture():
    return {
        "output_type": "execute_result",
        "data": {
            "text/plain": ["42"]
        }
    }

@pytest.fixture
def display_data_fixture():
    return {
        "output_type": "display_data",
        "data": {
            "text/plain": ["<DataFrame>"]
        }
    }

def test_format_output_execute_result(execute_result_fixture):
    result = format_output(execute_result_fixture)
    assert "**Result:**" in result
    assert "42" in result

def test_format_output_display_data(display_data_fixture):
    result = format_output(display_data_fixture)
    assert "**Display Data:**" in result
    assert "<DataFrame>" in result

def test_convert_notebook_auto_output_path(tmp_path):
    """Tests the case where output_path is not specified."""
    notebook_path = tmp_path / "auto_output.ipynb"
    expected_md_path = tmp_path / "auto_output.md"
    
    notebook_content = {"cells": [], "nbformat": 4, "nbformat_minor": 2}
    notebook_path.write_text(json.dumps(notebook_content))

    stats = convert_notebook(str(notebook_path)) # output_path is None
    
    assert stats['output_path'] == str(expected_md_path)
    assert expected_md_path.exists()

def test_main_function_success(mocker, tmp_path):
    """Test the main function directly to get coverage."""
    notebook_path = tmp_path / "main_test.ipynb"
    notebook_path.write_text('{"cells": [], "nbformat": 4, "nbformat_minor": 2}')
    
    # Mock sys.argv to simulate command-line arguments
    mocker.patch('sys.argv', ['jmd.py', str(notebook_path)])
    
    # We need to import main here, after mocking argv
    from jmd import main
    
    # Mock sys.exit to prevent the test from stopping
    mocker.patch('sys.exit')
    
    # Mock print to capture output
    mock_print = mocker.patch('builtins.print')

    main()

    # Assert that the success message was printed
    mock_print.assert_any_call("✓ Conversion successful!")

def test_main_function_file_not_found(mocker):
    """Test the main function's FileNotFoundError handling."""
    mocker.patch('sys.argv', ['jmd.py', 'non_existent_file.ipynb'])
    from jmd import main
    mock_exit = mocker.patch('sys.exit')
    mock_print = mocker.patch('builtins.print')

    main()

    mock_print.assert_called_with("✗ Error: Input file not found at 'non_existent_file.ipynb'", file=sys.stderr)
    mock_exit.assert_called_once_with(1)
