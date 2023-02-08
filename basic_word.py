# file with class BasicWord
# named as it was wanted is SOW

class BasicWord:
    # word: str = ""
    # is_correct: bool = False                   # very useless flag
    # subwords: list[str] = []
    # minimal_length_of_subwords: int = 0        # I can live without it

    def __init__(self, word: str, sublist: list[str]):
        self.word = word
        self.subwords = sublist
        # self.minimal_length_of_subwords = 0        # and without in I can live

    def check_include(self, newword: str) -> bool:
        """ check that newword included in subwords list"""
        if newword in self.subwords:
            return True
        else:
            return False

    def subwords_counter(self) -> int:
        """ count of subwords and return it
        """
        return (self.subwords.__len__())

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

