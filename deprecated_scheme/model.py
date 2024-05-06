# file for the model class
# because we are using sqlite3 to store the data, we don't use this word with id in the json file
import random
class Word:
    def __init__(self,id,word,phonetics,correct,incorrect_list,word_example):
        self.id = id
        self.word = word
        self.phonetics = phonetics
        self.correct = correct
        self.incorrect_list = incorrect_list
        self.word_example = word_example
    def __str__(self):
        return f'{self.id} {self.word} {self.phonetics} {self.correct} {self.incorrect_list} {self.word_example}'
    def choose_word(self,data):
        self.incorrect_list = random.choices(data, k=3)
        self.correct = self.word
        list_of_word = self.word_example.split(" ")
        for i in list_of_word:
            # find the word in the sentence
            if i == self.word:
                index = list_of_word.index(i)
                # replace the word with blank of the same length
                list_of_word = list_of_word[:index-1] + ["_" * len(self.word)] + list_of_word[index+1:]
        self.word_example = " ".join(list_of_word)
        