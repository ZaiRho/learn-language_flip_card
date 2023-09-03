import pandas
import pandas as pd
import random

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

# df_dict = df.to_dict(orient="records")
data_dict = df.to_dict()
data_dict_fr = data_dict["French"]
data_dict_en = data_dict["English"]
list_fr = [data_dict_fr[i] for i in range(len(data_dict_fr))]
list_en = [data_dict_en[i] for i in range(len(data_dict_en))]


class WordManager:
    def __init__(self):
        pass

    def get_word(self):
        ran_num = random.randint(0, len(list_fr)-1)
        word_fr = list_fr[ran_num]
        word_en = list_en[ran_num]
        word = {"FR": word_fr,
                "EN": word_en
                }
        return word

    def learn_word(self, word_fr, word_en):
        list_fr.remove(word_fr)
        list_en.remove(word_en)
        self.save_data()

    def save_data(self):
        new_dict = {
            "French": list_fr,
            "English": list_en
        }
        data_frame = pandas.DataFrame(new_dict)
        data_frame.to_csv("data/words_to_learn.csv")


