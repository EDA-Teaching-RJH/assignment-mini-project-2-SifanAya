from race_engine.validators import validate_bet

def test_logic():
    assert validate_bet("£100") == 100
    assert validate_bet("50") == 50
    assert validate_bet("1") == 1
    assert validate_bet("abc") is None