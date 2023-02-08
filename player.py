# file with class Player

class Player:
    # name: str = ""
    # used_words: list[str] = []

    def __init__(self, name: str):
        self.name = name
        self.used_words: list[str] = []

    def check_word_already_used(self, newword: str) -> bool:
        """ check that newword included in words list
            return True if already used
        """
        if newword in self.used_words:
            return True
        else:
            return False

    def used_words_counter(self) -> int:
        """ count of used_words and return it
        """
        return( self.used_words.__len__() )

    def append(self, newword: str):
        """ only append new word in used_word list. nothing to return"""
        self.used_words.append(newword)

    def __repr__(self) -> str:
        return f"Player({self.name}), used words = {str(self.used_words)}"