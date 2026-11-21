from src.core.job.mapper import Mapper
from src.student_jobs.decorators import map_words


class WordCountMapper(Mapper):
    @map_words
    def map(self, word, emit):
        emit(word, 1)
