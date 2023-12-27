def main():
    iterations = int(input("Testcases: "))

    for _ in range(iterations):
        worst_case()


def worst_case():
    max_t, max_n, sum_n = input("").split(" ")
    max_t = int(max_t)
    max_n = int(max_n)
    sum_n = int(sum_n)
    j = 0
    worst_iterations = 0
    while max_t != 0:
        if max_n <= sum_n:
            j += 1
            sum_n = sum_n - max_n
            max_t -= 1
        else:
            break

    for _ in range(j):
        worst_iterations += (max_n * max_n)
    if sum_n != 0 and max_t != 0:
        worst_iterations += (sum_n * sum_n)

    print(worst_iterations)


if __name__ == "__main__":
    main()
