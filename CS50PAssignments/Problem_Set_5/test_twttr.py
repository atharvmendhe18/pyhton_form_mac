from twttr_copy import remove_vowel


def test_remove_vowel_lower_case():
    assert remove_vowel("twitter") == 'twttr'


def test_remove_vowel_UPPER_CASE():
    assert remove_vowel('TWITTER') == 'TWTTR'


def test_remove_vowel_all_cases():
    assert remove_vowel('TwITter') == 'TwTtr'
