
#this is a script to test adding new words to the database
import sys,os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from manage import add_new_word

new_word = [
    {
        "word": "black",
        "correct": "A round fruit with seeds.",
        "incorrect": [
          "A type of bird.",
          "An underwater creature.",
          "A mode of transportation."
        ],
        "example": "I enjoy eating a juicy apple for breakfast."
      },
      {
        "word": "banana",
        "correct": "A long, yellow fruit.",
        "incorrect": [
          "A type of bird.",
          "An underwater creature.",
          "A mode of transportation."
        ],
        "example": "I enjoy eating a banana with my cereal."
      }
]
add_new_word(new_word)
