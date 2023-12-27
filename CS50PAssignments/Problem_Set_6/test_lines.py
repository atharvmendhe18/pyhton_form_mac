from lines import check_if_line_is_blank, check_if_line_is_comment


def test_check_if_line_is_comment_true():
    assert check_if_line_is_comment('#hello wortwrfwwrg') == True


def test_check_if_line_is_comment_false():
    assert check_if_line_is_comment('hello wortwrfwwrg') == False


def test_check_if_line_is_blank_true():
    assert check_if_line_is_blank('    ') == True


def test_check_if_line_is_blank_false():
    assert check_if_line_is_blank('afefeff     egegeg') == False
