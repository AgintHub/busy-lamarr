# implementcodecapplication PRD

## Description
Implement the application of various codecs to binary data


## Conceptual Info

This node generates code for applying various codecs to binary data read from files, utilizing the supported codecs and binary data reader function defined in parent nodes.

## Docstring

### Summary
Generates code to apply supported codecs to binary data.

### Parameters

- **supported_codecs** (List[str]): List of codec names supported by the CLI tool, provided by the 'definesupportedcodecs' node.
- **binary_data_reader_function** (str): Name of the function that reads binary data, provided by the 'implementbinarydatareader' node.

### Returns

str: Code snippet that demonstrates how to apply the supported codecs to binary data.

### Raises

- ValueError: If the list of supported codecs is empty or if the binary data reader function name is invalid.

### Examples

```python
>>> def apply_codecs(supported_codecs, binary_data_reader_function):
...     # Example implementation
...     code_snippet = ''
...     for codec in supported_codecs:
...         code_snippet += f'data = {binary_data_reader_function}(file_path).decode({codec})
'
...     return code_snippet
>>> supported_codecs = ['utf-8', 'ascii']
>>> binary_data_reader_function = 'read_binary_data'
>>> print(apply_codecs(supported_codecs, binary_data_reader_function))
data = read_binary_data(file_path).decode('utf-8')
data = read_binary_data(file_path).decode('ascii')
```
