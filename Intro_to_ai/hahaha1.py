def check_prime(no):
    for i in range(2, no):
        if no % i == 0:
            return False

    return True


print(check_prime(3))
