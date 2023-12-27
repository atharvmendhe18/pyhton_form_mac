class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Negative capacity not possible')
        else:
            self._capacity = capacity

        self._cookies = 0

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError('Not enough space in the jar')
        else:
            self._cookies += n

    def withdraw(self, n):
        if self._cookies - n < 0:
            raise ValueError('Not enought cookies in the jar')
        else:
            self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies


def main():
    jar = Jar(23)
    jar.deposit(5)
    jar.withdraw(2)
    print(jar.size)
    print(jar)
    print(jar.capacity)


if __name__ == "__main__":
    main()
