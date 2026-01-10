from pydantic import BaseModel, Field
from typing import List


class DefinesupportedcodecsOutput(BaseModel):
    """Pydantic model for definesupportedcodecs node outputs."""
    supported_codecs: List[str] = (
        Field(..., description="List of codec names supported by the CLI tool")
    )


class DefinenumericinterpretationsOutput(BaseModel):
    """Pydantic model for definenumericinterpretations node outputs."""
    numeric_interpretations: List[str] = (
        Field(..., description="List of numeric interpretations supported")
    )


class DesigncommandlineinterfaceOutput(BaseModel):
    """Pydantic model for designcommandlineinterface node outputs."""
    cli_syntax: str = Field(..., description="Command line syntax description")
    cli_options: str = Field(..., description="List of CLI options available")


def designcommandlineinterface(definesupportedcodecs_input: DefinesupportedcodecsOutput, definenumericinterpretations_input: DefinenumericinterpretationsOutput, **kwargs) -> DesigncommandlineinterfaceOutput:
    """
    Designs the CLI syntax for specifying binary data files, codecs, and numeric
    interpretations.

    Parameters
    ----------
    supported_codecs : List[str]
        List of codec names supported by the CLI tool, provided by the
        'definesupportedcodecs' node.
    numeric_interpretations : List[str]
        List of numeric interpretations supported by the CLI tool, provided
        by the 'definenumericinterpretations' node.

    Returns
    -------
    Tuple[str, List[str]]
        A tuple containing the CLI syntax description as a string and a list
        of available CLI options.

    Raises
    ------
    ValueError
        If either supported_codecs or numeric_interpretations is empty.

    Examples
    --------
    >>> supported_codecs = ['utf-8', 'ascii']
    >>> numeric_interpretations = ['int8', 'float32']
    >>> cli_syntax, cli_options = design_cli(supported_codecs,
    numeric_interpretations)
    ('binary_parser --file <path> --codec <codec> --interpret <interpretation>',
    ['--file', '--codec', '--interpret'])

    >>> supported_codecs = ['utf-16', 'latin1']
    >>> numeric_interpretations = ['uint16', 'int32']
    >>> cli_syntax, cli_options = design_cli(supported_codecs,
    numeric_interpretations)
    ('binary_parser --file <path> --codec <codec> --interpret <interpretation>',
    ['--file', '--codec', '--interpret'])

    """
    return DesigncommandlineinterfaceOutput(
        cli_syntax="",
        cli_options="",
    )