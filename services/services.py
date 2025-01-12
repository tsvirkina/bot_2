import random
from lexicon.lexicon import LEXICON_RU

def get_bot_choice()->str:
    return random.choice(['rock','scissors','paper'])

def _normalize_user_answer(user_answer:str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key

def get_winner(user_choise: str, bot_choise:str) -> str:
    user_choise = _normalize_user_answer(user_choise)
    rules = {
        'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'
    }

    if user_choise== bot_choise:
        return 'nobody_won'
    elif rules[user_choise] == bot_choise:
        return 'user_won'
    else:
        return 'bot_won'