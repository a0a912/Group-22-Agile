import requests, json ,random
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
                my_word_incorrect_meaning_list = word["incorrect"]
                break
        return my_word,my_word_phonetics,my_word_meaning,my_word_incorrect_meaning_list

if __name__ == "__main__":
    # an empty list to store the processed words (objects of Word class)
    list_of_words_processed = []
    # get the words we have in the json file, this words are not processed, with only the word, and 4 meanings, 1 correct and 3 incorrect
    with open("data.json","r",encoding="utf-8") as file:
        data = json.load(file)
        for word in data:
            word_tuple = get_meaning_phone(word["word"])
            # make it into an object
            word_for_question = Word(word_tuple[0],word_tuple[1],word_tuple[2],word_tuple[3]).__dict__
            list_of_words_processed.append(word_for_question)
    # write the object into a json file
    with open(f'./my_json.json', 'w') as file:
        json.dump(list_of_words_processed,file, indent=4)


"""
Maybe we can use sqlite3 to store the data later
"""
