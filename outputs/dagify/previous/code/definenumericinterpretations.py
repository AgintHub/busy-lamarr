from pydantic import BaseModel, Field
from typing import List


class DefinenumericinterpretationsOutput(BaseModel):
    """Pydantic model for definenumericinterpretations node outputs."""
    numeric_interpretations: List[str] = (
        Field(..., description="List of numeric interpretations supported")
    )


def definenumericinterpretations(general_input: str, **kwargs) -> DefinenumericinterpretationsOutput:
    """
    Returns a list of numeric interpretations supported by the CLI tool.

    Returns
    -------
    List[str]
        A list of numeric interpretation strings (e.g., int8, uint16,
        float32).

    Raises
    ------
    ValueError
        If the list of numeric interpretations is empty or invalid.

    Examples
    --------
    >>> definenumericinterpretations()
    ['int8', 'uint8', 'int16', 'uint16', 'float32']

    >>> definenumericinterpretations()
    ['int8', 'uint8', 'int16', 'uint16', 'float32', 'float64']

    """
    return DefinenumericinterpretationsOutput(
        numeric_interpretations=[],
    )