import re

def validate_bet(bet_str):
        if re.match(r"^£?\d+$", bet_str):
        clean_bet = bet_str.replace("£", "")
        return int(clean_bet)
    return None