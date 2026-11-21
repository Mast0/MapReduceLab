from src.core.job.reducer import Reducer


class VowelConsonantReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0
        for vowels, consonants in values:
            total_vowels += vowels
            total_consonants += consonants

        total = total_vowels + total_consonants
        if total > 0:
            vowel_pct = total_vowels / total * 100
            consonant_pct = total_consonants / total * 100
            emit(key, f"{vowel_pct:.2f}% голосних, {consonant_pct:.2f}% приголосних")
