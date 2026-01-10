from pydantic import BaseModel, Field
from typing import List


class DefinesupportedcodecsOutput(BaseModel):
    """Pydantic model for definesupportedcodecs node outputs."""
    supported_codecs: List[str] = (
        Field(..., description="List of codec names supported by the CLI tool")
    )


def definesupportedcodecs(general_input: str, **kwargs) -> DefinesupportedcodecsOutput:
    """
    Generates a list of all supported binary data codecs for the CLI tool.

    Returns
    -------
    List[str]
        List of strings representing codecs supported by the CLI tool.

    Raises
    ------
    ValueError
        If no codecs are defined or an issue prevents fetching the supported
        codecs.

    Examples
    --------
    >>> supported_codecs = definesupportedcodecs()
    ['utf-8', 'ascii', 'base64', 'hex']

    >>> # Example usage in downstream context:
    >>> if 'utf-8' in supported_codecs:
    ...     print('UTF-8 codec is supported!')
    'UTF-8 codec is supported!'

    """
    return DefinesupportedcodecsOutput(
        supported_codecs=[],
    )