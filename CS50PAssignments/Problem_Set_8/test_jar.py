from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(23)
    assert jar.capacity == 23


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    assert jar.cookies == 0
    jar.deposit(2)
    assert jar.cookies == 2
    jar.deposit(5)
    assert jar.cookies == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.cookies == 8
