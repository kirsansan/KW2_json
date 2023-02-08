'''the simple class for inputting and chesk strings'''


class InputAndCheckString:
    input_string: str = ""
    is_correct: bool = False
    is_empty: bool = True

    def __init__(self, input_string: str):
        self.input_string = input_string
        self.is_correct = False
        self.is_empty = self.verify_empty()

    def verify_empty(self) -> bool:
        '''check that string is empty or not'''
        if self.input_string == "":
            self.is_correct = False
            self.is_empty = True
            return True
        else:
            self.is_correct = True
            self.is_empty = False
            return False

    def verify_correct(self) -> bool:
        ''' check for something characteristic of string. for instance including only dots and minuses'''
        if (self.input_string).replace(".", "").replace("-", "") == "":   #only dot's and minuses w/o anything else
            return True
        else:
            self.is_correct = False
            return False

    def input_while_correct(self, incomment: str):
        '''I am going request you while you enter non-empty string
           also all strings will be rebuild to lowercase
        '''
        self.input_string = ""
        self.is_correct = False
        while not self.is_correct:
            #print(incomment)
            self.input_string = input(incomment)
            self.verify_empty()  # it can change is_correct flag
            self.input_string = self.input_string.lower()

    def input_empty(self, incomment: str):
        '''I am going request you while you enter EMPTY string
           don't ask me why customer wan't entering Enter only. It is a part of SOW
        '''
        #self.input_string = ""
        self.is_empty = False
        while not self.is_empty:
            print(incomment)
            self.input_string = input()
            self.verify_empty()  # it can change is_empty flag
