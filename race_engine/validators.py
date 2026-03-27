import re
def validate_bet(text):
    return bool(re.fullmatch(r"\d+", text))