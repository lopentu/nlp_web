from typing import List, Union


def clean_data(data: str) -> Union[str, List[str]]:
    """The clean_data function cleans the `data`. 

    Args:
        data (str): the input data
    Returns:
        a list of strings if the data is not None or an empty string, an
        empty string otherwise.
    """

    if (not data) or (data == ""):
        return ""

    data_list = data.split("\n")

    is_empty_list = all(map(lambda value: value == "", data_list))

    if is_empty_list:
        return ""

    filtered_list = filter(None, data_list)
    return list(map(lambda value: value.strip(), filtered_list))
