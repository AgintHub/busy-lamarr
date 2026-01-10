from pydantic import BaseModel, Field


class ImplementbinarydatareaderOutput(BaseModel):
    """Pydantic model for implementbinarydatareader node outputs."""
    binary_data_reader_function: str = (
        Field(..., description="Name of the function that reads binary data")
    )


def implementbinarydatareader(general_input: str, **kwargs) -> ImplementbinarydatareaderOutput:
    """
    Implements a function to read binary data from a file and returns the name
    of this function.

    Parameters
    ----------
    file_path : str
        Path to the file from which to read binary data.

    Returns
    -------
    str
        Name of the function that reads binary data from the specified file
        path.

    Raises
    ------
    FileNotFoundError
        If the file at the specified path does not exist.
    IOError
        If there's an issue reading the file.

    Examples
    --------
    >>> read_binary_data('example.bin')
    'read_binary_data'

    >>> read_binary_data('non_existent_file.bin')
    FileNotFoundError: File 'non_existent_file.bin' not found.

    """
    return ImplementbinarydatareaderOutput(
        binary_data_reader_function="",
    )