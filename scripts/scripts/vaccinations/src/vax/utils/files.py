import os
import json
from pathlib import Path


STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_static"))
QUERIES_DIR = os.path.abspath(os.path.join(STATIC_DIR, "queries"))


def load_query(query_filename: str, file_ext: str = "json"):
    """Load a query from a file in vax._static folder.

    Args:
        query_filename (str): Name of the query file. If no extension is provided, {query_filename}.{file_ext} will be 
                                loaded
        file_ext (str, optional): Extension of the file. Defaults to "json".

    Raises:
        FileNotFoundError: If no file is found
        ValueError: If non-supported format is provided

    Returns:
        dict: Loaded query as a string
    """
    filename_path = os.path.join(QUERIES_DIR, query_filename)
    if not os.path.isfile(filename_path):
        query_filename = f"{Path(query_filename).stem}.{file_ext}"
        filename_path = os.path.join(QUERIES_DIR, query_filename)
        if not os.path.isfile(f"{filename_path}"):
            raise FileNotFoundError(f"File {filename_path} not found")
    if file_ext == "json": 
        with open(filename_path) as f:
            data = str(json.load(f))
    else:
        raise ValueError("Only JSON format supported")
    return data
