import json
import os
from config import DATABASE


def load_db():

    if not os.path.exists(DATABASE):

        save_db({
            "bots":[]
        })


    with open(
        DATABASE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_db(data):

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def add_bot(bot):

    db=load_db()

    db["bots"].append(bot)

    save_db(db)



def get_bots():

    return load_db()["bots"]
