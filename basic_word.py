# file with class BasicWord
# named as it was wanted is SOW

class BasicWord:

    def __init__(self, word: str, sublist: list[str]):
        self.word = word
        self.subwords = sublist

    def check_include(self, newword: str) -> bool:
        """ check that newword included in subwords list"""
        if newword in self.subwords:  # will check only lower words. subwords already lower by default
            return True
        return False

    def subwords_counter(self) -> int:
        """Сount of subwords and return it"""
        return len(self.subwords)

    def calculete_minimal_length_of_sub(self) -> int:
        """Find the shortest element in subwords and return his length
           work only if self include minimum one element
        """
        tmp_length = len(self.subwords[0])
        for sub in self.subwords:
            if tmp_length > len(sub):
                tmp_length = len(sub)
        return tmp_length

    def __repr__(self) -> str:
        return f"BasicWord({self.word}, {str(self.subwords)})"
