from plates_copy import is_valid


def test_correct():
    assert is_valid('cs50') == True


def test_no_in_between():
    assert is_valid('abc23e') == False


def test_first_no_zero():
    assert is_valid('abcd03') == False


def test_min_length():
    assert is_valid('A') == False


def test_max_lenght():
    assert is_valid('abcd12345') == False
