import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # количество попыток
    count = 0

    list_num = list(range(1, 101))
    first = 1
    last = len(list_num) - 1

    while first <= last:
        count += 1
        midpoint = int((first + last) / 2)
        if list_num[midpoint] == number:
            break  # выход из цикла если угадали
        else:
            if number < list_num[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
