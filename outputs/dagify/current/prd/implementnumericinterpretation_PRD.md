# implementnumericinterpretation PRD

## Description
Implement the interpretation of binary data as different numeric types


## Conceptual Info

This node generates code to interpret binary data as various numeric types defined in the 'definenumericinterpretations' node, using the binary data reader function from 'implementbinarydatareader'.

## Docstring

### Summary
Generates code for interpreting binary data as different numeric types.

### Parameters

- **numeric_interpretations** (List[str]): List of numeric interpretations supported, provided by 'definenumericinterpretations'.
- **binary_data_reader_function** (str): Name of the function that reads binary data, provided by 'implementbinarydatareader'.

### Returns

str: Code snippet that interprets binary data as the defined numeric types.

### Raises

- ValueError: If numeric_interpretations is empty or binary_data_reader_function is not a valid function name.

### Examples

```python
>>> numeric_interpretations = ['int8', 'uint16', 'float32']
>>> binary_data_reader_function = 'read_binary_data'
>>> interpret_binary_data(numeric_interpretations, binary_data_reader_function)
"""
import numpy as np
def interpret_binary_data(data, interpretation):
    if interpretation == 'int8':
        return np.frombuffer(data, dtype=np.int8)
    elif interpretation == 'uint16':
        return np.frombuffer(data, dtype=np.uint16)
    elif interpretation == 'float32':
        return np.frombuffer(data, dtype=np.float32)
    else:
        raise ValueError('Unsupported interpretation')
"""
```
