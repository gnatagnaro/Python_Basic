print('Задача 4. Калькулятор скидки')

# Васин друг переехал в новую квартиру, и ему нужно купить три стула в разные комнаты. Цены на стулья  разные, а в некоторых магазинах есть скидки. Друг хочет заказать у Васи калькулятор скидки, чтобы проще ориентироваться в ценах.

# Напишите программу, которая запрашивает три стоимости товара и вычисляет сумму чека. Если сумма чека превышает 10 000 руб., нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). Итоговая сумма должна выводиться на экран.

price_1 = int(input('Введите стоимость товара: '))
price_2 = int(input('Введите стоимость товара: '))
price_3 = int(input('Введите стоимость товара: '))

sum = price_1 + price_2 + price_3

if sum > 10000:
    sum -= sum*0.1
print(sum)