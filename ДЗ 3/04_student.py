# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код

need_money = expenses - educational_grant
inflation = expenses
month = 0
while month < 10:
    if month == 0:
        month += 1
        print('Расходы в месяце', month, 'составили', round(need_money, 2))
    else:
        month += 1
        inflation *= 1.03
        need_money += inflation-educational_grant
        print('Расходы в месяце', month, 'составили', round(need_money, 2))

print('Надо попросить у родителей', round(need_money, 2), 'рублей')
