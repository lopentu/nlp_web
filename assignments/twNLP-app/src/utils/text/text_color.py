def create_pos_color(pos: str) -> str:
    """The create_color function creats a text color base on the `pos` type.
    Args:
        pos (str): part of speech
    Returns:
        a str (e.g. 'rgb(255,0,0)' or '#ff0000')
    """

    if len(pos) >= 4:
        return "rgb(102, 102, 102)"

    pos_color_factories = {
        "A": "rgb(21, 170, 191)",
        "C": "rgb(231, 41, 138)",
        "D": "rgb(117, 112, 179)",
        "I": "rgb(102, 166, 30)",
        "N": "rgb(27, 158, 119)",
        "P": "rgb(102, 166, 30)",
        "S": "rgb(166, 118, 29)",
        "T": "rgb(102, 166, 30)",
        "V": "rgb(217, 95, 2)",
        "F": "rgb(230, 171, 2)",
    }

    return pos_color_factories[pos[0]]


def create_entity_color(entity: str):
    """The create_color function creats a text color base on the `entity` type.
    Args:
        entity (str): an entity type from the result of NER
    Returns:
        a str (e.g. 'rgb(255,0,0)' or '#ff0000')
    """

    entity_color_factories = {
        "GPE": "rgb(102, 166, 30)",
        "PERSON": "rgb(166, 118, 29)",
        "DATE": "rgb(217, 95, 2)",
        "ORG": "rgb(102, 166, 30)",
        "CARDINAL": "rgb(27, 158, 119)",
        "ORDINAL": "rgb(231, 41, 138)",
        "NORP": "rgb(117, 112, 179)",
        "LOC": "rgb(27, 158, 119)",
        "TIME": "rgb(117, 112, 179)",
        "FAC": "rgb(231, 41, 138)",
        "MONEY": "rgb(217, 95, 2)",
        "ORDINAL": "rgb(231, 41, 138)",
        "EVENT": "rgb(117, 112, 179)",
        "WORK_OF_ART": "rgb(231, 41, 138)",
        "QUANTITY": "rgb(217, 95, 2)",
        "PERCENT": "rgb(230, 171, 2)",
        "LANGUAGE": "rgb(230, 171, 2)",
        "PRODUCT": "rgb(27, 158, 119)",
        "LAW": "rgb(166, 118, 29)",
    }
    return entity_color_factories[entity]
