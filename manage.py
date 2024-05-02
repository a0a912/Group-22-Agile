import requests, json ,random,os
from pathlib import Path
from model import Word


# a function to get the meaning of the word
def get_meaning_phone(word):
    # using the api of dictionary to get information about the word
    response_of_meaning = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    if response_of_meaning.status_code == 200:
        word_original_json = response_of_meaning.json()[0]
        # get the word
        my_word = word_original_json["word"]
        # get the phonetics
        if word_original_json["phonetics"][0]["audio"] != "":
            my_word_phonetics = word_original_json["phonetics"][0]["audio"]
        elif word_original_json["phonetics"][1]["audio"] != "":
            my_word_phonetics = word_original_json["phonetics"][1]["audio"]
        else:
            my_word_phonetics = ""
            print("No audio available")
        # get the meaning
        for word in data:
            if word["word"] == my_word:
                my_word_meaning = word["correct"]
                my_word_incorrect_list = word["incorrect"]
                my_word_example = word["example"]
                break
        return my_word,my_word_phonetics,my_word_meaning,my_word_incorrect_list,my_word_example

if __name__ == "__main__":
    # an empty list to store the words themselves
    list_of_words = []
    # an empty list to store the processed words (objects of Word class)
    list_of_words_processed = []
    # an empty list to store the processed words with blanks (objects of Word class)
    list_of_words_blank = []
    # get the words we have in the json file, this words are not processed, with only the word, and 4 meanings, 1 correct and 3 incorrect
    with open("data.json","r",encoding="utf-8") as file:
        data = json.load(file)
        for word in data:
            list_of_words.append(word["word"])
        for word in data:
            word_tuple = get_meaning_phone(word["word"])
            # make it into an object
            word_for_question = Word(word_tuple[0],word_tuple[1],word_tuple[2],word_tuple[3],word_tuple[4])
            # make it into a dictionary for json
            word_for_question_dictionary = word_for_question.__dict__
            # append the dictionary into the list for json
            list_of_words_processed.append(word_for_question_dictionary)

            # second type of question, fill in the blank
            # make a sentence with the word picked out, and replace the word with blank
            word_blank = Word(word_tuple[0],word_tuple[1],word_tuple[2],word_tuple[3],word_tuple[4])
            # randomly choose 3 words from the list of words to be the incorrect answers
            Word.choose_word(word_blank,list_of_words)
            list_of_words_blank.append(word_blank.__dict__)
    
    
    # write the object into a json file
    database_path = Path(f'./database')
    if not database_path.exists():
        Path(f'./database').mkdir()
    database_explain_question = database_path.joinpath('my_json.json')
    with open(database_explain_question , 'w') as file:
        json.dump(list_of_words_processed,file, indent=4)

    database_fill_question = database_path.joinpath('fill_in_the_blank.json')
    with open(database_fill_question, 'w') as file:
        json.dump(list_of_words_blank,file, indent=4)


"""
Maybe we can use sqlite3 to store the data later
"""
