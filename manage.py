import requests, json ,random,os
from pathlib import Path
from model import Word


# a function to get the meaning of the word
# the function takes in the word and the data from the json file
def get_meaning_phone(word,data):
    # using the api of dictionary to get information about the word
    response_of_meaning = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    if response_of_meaning.status_code == 200:
        word_original_json = response_of_meaning.json()[0]
        # get the word
        my_word = word_original_json["word"]
        # get the phonetics
        if word_original_json["phonetics"][0]["audio"] != "":
            word_phonetics = word_original_json["phonetics"][0]["audio"]
        elif word_original_json["phonetics"][1]["audio"] != "":
            word_phonetics = word_original_json["phonetics"][1]["audio"]
        else:
            word_phonetics = ""
            print("No audio available")
        # get the meaning
        for word in data:
            if word["word"] == my_word:
                word_meaning = word["correct"]
                word_incorrect_list = word["incorrect"]
                word_example = word["example"]
                break
        return my_word,word_phonetics,word_meaning,word_incorrect_list,word_example
# get the existing words in the json file
def get_existing_words(path):
    with open(path,"r",encoding="utf-8") as file:
        data = json.load(file)
        word_list = [word["word"] for word in data]
        return word_list

# a function to add new words into the json file
def add_new_word(json_list):
    database_fill_question = Path(f'./database/fill_in_the_blank.json')
    choose_definition_question = Path(f'./database/my_json.json')
    list_of_path = [choose_definition_question,database_fill_question]
    # an empty list to store the processed words (objects of Word class) without id, we need to know the last id in the list to assign the id
    list_of_object_without_id = []
    # get the existing words in the json file
    list_of_words= get_existing_words(database_fill_question)
    for word in json_list:
        the_word = word["word"]
        if the_word == "":
            print("word is empty")
        elif the_word in list_of_object_without_id or the_word in list_of_words: 
            print(f"word {the_word} already exists")
        else:
            [my_word,word_phonetics,word_meaning,word_incorrect_list,word_example] = get_meaning_phone(word["word"],json_list)
            word_for_question = Word(0,my_word,word_phonetics,word_meaning,word_incorrect_list,word_example)
            list_of_object_without_id.append(word_for_question)
    if list_of_object_without_id == []:
        print("No new word to add")
        return None
    # get the words we have in the json file, this words are not processed, with only the word, and 4 meanings, 1 correct and 3 incorrect
    for i in list_of_path:
        with open(i,"r",encoding="utf-8") as file:
            data = json.load(file)
            # find the length of the list
            length = len(data)
            # find the last id in the list
            last_id = data[length-1]["id"]+1
            # change the word id following the last id in the list
            for word_for_question in list_of_object_without_id:
                if i == database_fill_question: 
                    # for fill in the blank questions, we need to choose 3 incorrect answers
                    Word.choose_word(word_for_question,list_of_words)
                    word_for_question_dict=word_for_question.__dict__
                    word_for_question_dict["id"] = last_id + list_of_object_without_id.index(word_for_question)
                else:
                    # for choose definition questions, we don't need to choose 3 incorrect answers
                    word_for_question_dict=word_for_question.__dict__
                    word_for_question_dict["id"] = last_id + list_of_object_without_id.index(word_for_question)
                # append the dictionary into the list for json
                data.append(word_for_question_dict)
        # write the object into a json file
        with open(i,"w",encoding="utf-8") as file:
            json.dump(data,file, indent=4)
        print("done")

if __name__ == "__main__":
    # an  list to store the words themselves
    list_of_words= get_existing_words("data.json")
    # an empty list to store the processed words (objects of Word class)
    list_of_words_processed = []
    # an empty list to store the processed words with blanks (objects of Word class)
    list_of_words_blank = []
    # get the words we have in the json file, this words are not processed, with only the word, and 4 meanings, 1 correct and 3 incorrect
    with open("data.json","r",encoding="utf-8") as file:
        data = json.load(file)
        for word in data:
            word_tuple = get_meaning_phone(word["word"],data)
            id = list_of_words.index(word["word"])+1
            # make it into an object
            word_for_question = Word(id,word_tuple[0],word_tuple[1],word_tuple[2],word_tuple[3],word_tuple[4])
            # make it into a dictionary for json
            word_for_question_dictionary = word_for_question.__dict__
            # append the dictionary into the list for json
            list_of_words_processed.append(word_for_question_dictionary)

            # second type of question, fill in the blank
            # make a sentence with the word picked out, and replace the word with blank
            word_blank = Word(id,word_tuple[0],word_tuple[1],word_tuple[2],word_tuple[3],word_tuple[4])
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
