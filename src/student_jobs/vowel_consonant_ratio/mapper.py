from src.core.job.mapper import Mapper
from src.student_jobs.decorators import map_words

VOWELS = set("аеєиіїоуюяaeiouy")
NON_SOUND_LETTERS = set("ь")


class VowelConsonantMapper(Mapper):
    @map_words
    def map(self, word, emit):
        vowels = sum(1 for ch in word if ch in VOWELS)
        consonants = sum(
            1
            for ch in word
            if ch.isalpha() and ch not in VOWELS and ch not in NON_SOUND_LETTERS
        )
        if vowels + consonants > 0:
            emit(len(word), (vowels, consonants))
