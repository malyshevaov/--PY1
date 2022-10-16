salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
count_month = 0
for i in range (months):
    if i == 0:
        spend = spend
        count_month += 1
        need_money = need_money + spend
    else:
        spend = spend * (1+increase)
        count_month += 1
        need_money = need_money + spend
money_from_salary = salary * months
money = need_money - money_from_salary

print(round(money))
