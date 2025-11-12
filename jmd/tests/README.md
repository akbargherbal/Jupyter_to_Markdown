# Test Cases

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
