from bank_copy import value


def testing_hello():
    assert value('hello') == '$0'


def test_str_starting_with_h():
    assert value('hi') == '$20'
    assert value('hilo') == '$20'


def test_other_str():
    assert value('Whats Up') == '$100'
    assert value('yo') == '$100'
