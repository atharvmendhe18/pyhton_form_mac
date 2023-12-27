from numb3rs_alt import validate


def test_validate_singledigit_correct():
    assert validate('1.2.1.3') == 'Valid'


def test_validate_doubledigit_correct():
    assert validate('13.45.99.56') == 'Valid'


def test_validate_3digit_correct():
    assert validate('145.202.144.123') == 'Valid'


def test_validate_singledigit_incorrect():
    assert validate('1.2.1') == 'invalid'


def test_validate_doubledigit_incorrect():
    assert validate('13.24.14') == 'invalid'


def test_validate_tripledigit_incorrect():
    assert validate('1.2.1.344') == 'invalid'
