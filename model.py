class Word:
    def __init__(self,word,phonetics,correct_meaning,incorrect_meaning_list,word_example):
        self.word = word
        self.phonetics = phonetics
        self.meaning = correct_meaning
        self.incorrect_meaning_list = incorrect_meaning_list
        self.word_example = word_example
    def __str__(self):
        return f'{self.word} {self.phonetics} {self.meaning} {self.incorrect_meaning_list} {self.word_example}'