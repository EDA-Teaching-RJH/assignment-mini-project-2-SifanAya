from race_engine.validators import validate_bet
def test_logic():
    assert validate_bet("100") == True
    assert validate_bet("abc") == False