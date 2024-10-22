money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_mounth = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital >0:
    money_capital = money_capital + salary - spend
    spend *= 1.05
    if money_capital<0:
        break
    count_mounth += 1



print(f"Количество месяцев, которое можно протянуть без долгов: {count_mounth}")
