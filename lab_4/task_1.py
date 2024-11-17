import json


# TODO решите задачу
def task() -> float:
    # Чтение данных из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисление суммы произведений
    total = sum(item['score'] * item['weight'] for item in data)

    # Округление до 3 знаков после запятой
    return round(total, 3)


print(task())
