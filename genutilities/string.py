def remove(text: str, to_remove):
    if isinstance(to_remove, (list, tuple)):
        for i in to_remove:
            text = text.replace(i, "")
    elif isinstance(to_remove, str):
        text = text.replace(to_remove, "")
    else:
        raise TypeError("Second Argument must be a list or a str.")
    return text