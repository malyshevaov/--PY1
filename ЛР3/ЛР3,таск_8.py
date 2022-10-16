money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
count_month = 0
total_capital = money_capital + salary
while total_capital >= 0:
    count_month += 1
    spend = spend * (1 + increase)
    total_capital = total_capital - spend
print(count_month)






