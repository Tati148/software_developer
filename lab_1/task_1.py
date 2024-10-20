numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_num = sum(filter(None, numbers))
len_num = len(numbers)

avg_num = sum_num / len_num

numbers[4] = avg_num

print("Измененный список:", numbers)

