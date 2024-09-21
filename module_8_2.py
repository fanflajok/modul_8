def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    kor = (result, incorrect_data)
    return kor
def calculate_average(numbers):
        try:
            len_ = len(numbers) - personal_sum(numbers)[1]
            avg = personal_sum(numbers)[0]/len_
            return avg
        except ZeroDivisionError:
            avg = 0
            return avg
        except TypeError:
            return 'В numbers записан некорректный тип данных'





# print(calculate_average([]))
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


