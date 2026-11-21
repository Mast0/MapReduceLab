import re
from functools import wraps

WORD_RE = re.compile(r"[а-яА-ЯіїєґІЇЄҐa-zA-Z]+(?:['’][а-яА-ЯіїєґІЇЄҐa-zA-Z]+)*")


def map_words(func):
    @wraps(func)
    def wrapper(self, record, emit):
        for match in WORD_RE.finditer(str(record)):
            word = match.group(0).lower().replace("’", "'")
            func(self, word, emit)

    return wrapper
