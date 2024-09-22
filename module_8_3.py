class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        if self.__is_valid_vin_number(__vin):
            self.__vin_number = int(__vin)
        if self.__is_valid_numbers(__numbers):
            self.__numbers = str(__numbers)
    def __is_valid_vin_number(self, __vin):
        if not isinstance(__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        elif not 1000000 <= __vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True
    def __is_valid_numbers(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


try:
  first = Car('Rapid', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  first = Car('Octavia', 8630263, 'K354TT')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Caroq', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Kodiaq', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')