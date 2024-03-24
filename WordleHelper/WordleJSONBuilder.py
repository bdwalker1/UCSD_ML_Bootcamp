import re
import pandas as pd
from datetime import datetime as dtm


def __readfiles() -> list:
    valid_word_df = pd.read_csv(
                "https://raw.githubusercontent.com/bdwalker1/UCSD_ML_Bootcamp/main/WordleHelper/wordle_valid_words.txt"
                )
    used_word_df = pd.read_csv(
                "https://raw.githubusercontent.com/bdwalker1/UCSD_ML_Bootcamp/main/WordleHelper/wordle_used_words.txt"
                )
    used_word_df.set_index("used_word", inplace=True)
    return [valid_word_df, used_word_df]


def buildjson() -> pd.DataFrame:
    """Use the full Wordle word list and the used word data to build a JSON"""

    dfs = __readfiles()
    valid_word_df, used_word_df = dfs
    valid_word_df.insert(len(valid_word_df.iloc[0]), "times_used", 0)
    valid_word_df.insert(len(valid_word_df.iloc[0]), "last_used", None)
    valid_word_df.insert(len(valid_word_df.iloc[0]), "dates_used", None)
    valid_word_df.set_index("valid_word", inplace=True)
    for index, row in valid_word_df.iterrows():
        if index in list(used_word_df.index.values):
            valid_word_df.at[index,"times_used"] += 1
            valid_word_df.at[index,"last_used"] = dtm.strptime(used_word_df.loc[index]["game_date"], "%m-%d-%Y")
            if valid_word_df.at[index, "dates_used"] is None:
                valid_word_df.at[index, "dates_used"] = list()
            valid_word_df.at[index, "dates_used"].append(dtm.strptime(used_word_df.loc[index]["game_date"], "%m-%d-%Y"))
    print(valid_word_df[valid_word_df['times_used'] > 0].head(20)["dates_used"])
    print(valid_word_df.to_json(orient="records"))
    return valid_word_df


if __name__ == '__main__':
    print("Dude, We are here!")
    buildjson()