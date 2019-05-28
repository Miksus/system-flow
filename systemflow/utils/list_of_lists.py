

def flatten(l):
    # https://stackoverflow.com/a/2158532
    for el in l:
        if isinstance(el, (tuple, list)) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el