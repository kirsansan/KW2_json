# This is a simple Python script. ;-)
# Coure work 2. Python 20 groupe
# writted by Kirill.S

from basic_word import BasicWord
from player import Player
from utils import load_random_word
from my_new_input.my_input import InputAndCheckString
import random

HELP_MODE = True


def main():

    # init variables block
    word_for_research: BasicWord = BasicWord("", [])  # custom class with words
    temp_word: str = ""  # temporary string
    correct_answer_counter: int = 0  # I can live without you, but I like counters
    lenth_limit: int = 3  # will be recaclulate

    input_and_check: InputAndCheckString = InputAndCheckString("")  # string for work with user

    # call load_random and create BasicWord from external data
    word_for_research = load_random_word()
    lengh_limit = int(word_for_research.calculete_minimal_length_of_sub())  # I promised recalculate it

    # create player's block
    input_and_check.input_while_correct("Ввведите имя игрока ")
    # if you wanted ask me why I named him "player1" I would answer you 'For a future. I dream update it for multiuser prog'
    player1: Player = Player(input_and_check.input_string)

    # let's go doing conversation with user
    print(f'Привет {player1.name}')
    print(f'составь {word_for_research.subwords_counter()} слов из слова {word_for_research.word}')
    print(f'Слова должны быть не короче {lengh_limit} букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите "stop"')

    # debug block.
    if HELP_MODE:
        print(word_for_research.subwords)  # open me if you want to see hints =)

    print("Поехали, ваше первое слово?")

    # checking words while
    while correct_answer_counter != word_for_research.subwords_counter():
        input_and_check.input_while_correct(">")
        temp_word = input_and_check.input_string.lower()    # was corrected by hint from couch (add lower())
        if temp_word == "stop" or temp_word == "стоп":
            # красиво уйти (we need beauty exit)
            print(f'Игра завершена, {player1.name}, вы угадали {player1.used_words_counter()} слов!')
            quit(0)
        else:
            if temp_word in word_for_research.subwords and not player1.check_word_already_used(temp_word):
                '''user add new correct word'''
                player1.append(temp_word)
                print('верно')
                correct_answer_counter += 1
            elif len(temp_word) <= lengh_limit - 1:
                print('слишком короткое слово')
            elif player1.check_word_already_used(temp_word):
                print('уже использовано')
            elif temp_word not in word_for_research.subwords:
                print('неверно. нет такого слова в этой букве.. точнее в этом списке ;-)')
            else:
                quit(1)  # this situation is not impossible but we will protect excepion and Moon phases

    # we will step to this string only if all words are corretly named. Bingo, firework and drumroll!
    print(f'Игра завершена, {player1.name}, вы угадали {player1.used_words_counter()} слов!')

    if True:
        print("Не везет в игре - повезет в любви (с) ")
    else:
        print("""Если вы проверяете этот код 
              - помогите мне получить доступ к урокам с 10 по 16.
              хотя я знаю, это почти не в ваших силах =((( """)
    quit(0)


# main block
if __name__ == '__main__':
    main()

# this is end of this short history
