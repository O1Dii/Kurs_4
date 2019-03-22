def main():
    from time import time
    from random import randint, shuffle
    from functools import reduce
    from copy import copy
    from math import pi

    iterations = 100
    size = 10_000_000
    my_sum = 0
    # arr = tuple(np.random.randint(0, 256, size))
    arr2 = tuple(range(1000))
    # arr2 = tuple(sorted([x for x in templist]))
    # arr1 = tuple([randint(0, 256) for i in range(size)])
    arr1 = list(copy(arr2))
    shuffle(arr1)
    arr1 = tuple(arr1)
    aproximate_result = sum(arr2) / 2
    number = 0
    while my_sum < aproximate_result:
        my_sum += number
        number += 1

    number -= 2
    average_number = number
    aproximate_result *= iterations

    print("Результат должен быть примерно - " + str(aproximate_result), sum(arr2), average_number, sep='\n')

    print("Лёха---------------")

    my_sum = 0
    start = time()
    for i in range(iterations):
        for j in arr1:
            if j > average_number:
                my_sum += j

    end = time()
    unsorted_result = end - start
    print("Время несортированного - " + str(unsorted_result), "Сумма - " + str(my_sum), sep='\n')
    arr2 = tuple(sorted(arr1))
    # print(type(arr))
    my_sum = 0
    start = time()
    for i in range(iterations):
        for j in arr2:
            if j > average_number:
                my_sum += j

    end = time()
    sorted_result = end - start
    print("Время сортированного - " + str(sorted_result), "Сумма - " + str(my_sum),
          "Результат - " + str(unsorted_result / sorted_result),
          "Разница от примерного - " + str(abs(aproximate_result - my_sum)), sep='\n')

    print("Кирилл-----------")
    my_sum = 0
    f = lambda summ, elem: summ + elem if elem > average_number else summ

    start = time()
    for _ in range(iterations):
        my_sum = reduce(f, arr1)
    end = time()

    unsorted_result = end - start
    print("Время несортированного - " + str(unsorted_result), "Сумма - " + str(my_sum), sep='\n')

    my_sum = 0

    start = time()
    for _ in range(iterations):
        my_sum = reduce(f, arr1)
    end = time()

    sorted_result = end - start
    print("Время сортированного - " + str(sorted_result), "Сумма - " + str(my_sum),
          "Результат - " + str(unsorted_result / sorted_result),
          "Разница от примерного - " + str(abs(aproximate_result - my_sum)), sep='\n')


# def sum(summ, elem):
#     return summ + elem if elem > 128 else summ
# lambda summ, elem: summ + elem if elem > 128 else summ


if __name__ == '__main__':
    main()
