# designcommandlineinterface PRD

## Description
Design the CLI syntax for specifying binary data files, codecs, and numeric interpretations


## Conceptual Info

This node designs the command line interface (CLI) syntax for a binary data parsing tool, incorporating supported codecs and numeric interpretations from its parent nodes.

## Docstring

### Summary
Designs the CLI syntax for specifying binary data files, codecs, and numeric interpretations.

### Parameters

- **supported_codecs** (List[str]): List of codec names supported by the CLI tool, provided by the 'definesupportedcodecs' node.
- **numeric_interpretations** (List[str]): List of numeric interpretations supported by the CLI tool, provided by the 'definenumericinterpretations' node.

### Returns

Tuple[str, List[str]]: A tuple containing the CLI syntax description as a string and a list of available CLI options.

### Raises

- ValueError: If either supported_codecs or numeric_interpretations is empty.

### Examples

```python
>>> supported_codecs = ['utf-8', 'ascii']
>>> numeric_interpretations = ['int8', 'float32']
>>> cli_syntax, cli_options = design_cli(supported_codecs, numeric_interpretations)
('binary_parser --file <path> --codec <codec> --interpret <interpretation>', ['--file', '--codec', '--interpret'])
```

```python
>>> supported_codecs = ['utf-16', 'latin1']
>>> numeric_interpretations = ['uint16', 'int32']
>>> cli_syntax, cli_options = design_cli(supported_codecs, numeric_interpretations)
('binary_parser --file <path> --codec <codec> --interpret <interpretation>', ['--file', '--codec', '--interpret'])
```
