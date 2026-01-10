# implementbinarydatareader PRD

## Description
Implement a module to read binary data from files


## Conceptual Info

This node implements a function to read binary data from a specified file path, returning the name of the function that performs this operation.

## Docstring

### Summary
Implements a function to read binary data from a file and returns the name of this function.

### Parameters

- **file_path** (str): Path to the file from which to read binary data.

### Returns

str: Name of the function that reads binary data from the specified file path.

### Raises

- FileNotFoundError: If the file at the specified path does not exist.
- IOError: If there's an issue reading the file.

### Examples

```python
>>> read_binary_data('example.bin')
'read_binary_data'
```

```python
>>> read_binary_data('non_existent_file.bin')
FileNotFoundError: File 'non_existent_file.bin' not found.
```
