def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данный для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not hasattr(numbers, '__iter__'):
            raise TypeError('В numbers записан некорректный тип данных')

        total, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data

        average = total / count if count > 0 else 0
        return average

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('е')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')