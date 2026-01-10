# definenumericinterpretations PRD

## Description
Define various numeric interpretations supported by the CLI tool


## Conceptual Info

This node defines the various numeric interpretations that the CLI tool will support for parsing binary data.

## Docstring

### Summary
Returns a list of numeric interpretations supported by the CLI tool.

### Returns

List[str]: A list of numeric interpretation strings (e.g., int8, uint16, float32).

### Raises

- ValueError: If the list of numeric interpretations is empty or invalid.

### Examples

```python
>>> definenumericinterpretations()
['int8', 'uint8', 'int16', 'uint16', 'float32']
```

```python
>>> definenumericinterpretations()
['int8', 'uint8', 'int16', 'uint16', 'float32', 'float64']
```
