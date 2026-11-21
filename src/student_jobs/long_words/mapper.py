from src.core.job.mapper import Mapper
from src.student_jobs.decorators import map_words


class LongWordsMapper(Mapper):
    @map_words
    def map(self, word, emit):
        if len(word) > 5:
            emit(word, 1)
