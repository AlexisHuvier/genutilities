import string
import random as rand

def remove(text: str, to_remove):
    if isinstance(to_remove, (list, tuple)):
        for i in to_remove:
            text = text.replace(i, "")
    elif isinstance(to_remove, str):
        text = text.replace(to_remove, "")
    else:
        raise TypeError("Second Argument must be a list or a str.")
    return text

def random(n=30, letters = string.ascii_letters + string.digits + string.punctuation + " "):
    return ''.join(rand.choice(letters) for i in range(n))

def reverse(text: str):
    return text[::-1]

def shuffle(text: str):
    return ''.join(rand.sample(text, len(text)))

def unique(text: str):
    l = []
    for i in text:
        if i not in l:
            l.append(i)
    return ''.join(l)

def snake_to_pascal(text: str):
    l = text.split("_")
    return "".join([i.capitalize() for i in l])

def pascal_to_snake(text: str):
    l = []
    for i in text:
        if i in string.ascii_uppercase:
            if l != []:
                l.append("_")
            l.append(i.lower())
        else:
            l.append(i)
    return "".join(l)

camel_to_snake = pascal_to_snake

def pascal_to_camel(text: str):
    if len(text):
        text = text[0].lower() + text[1:]
    return text

def camel_to_pascal(text: str):
    return text[0].upper() + text[1:]

def snake_to_camel(text: str):
    return pascal_to_camel(snake_to_pascal(text))