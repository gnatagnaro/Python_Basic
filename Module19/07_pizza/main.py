num_orders = int(input('Введите кол-во заказов: '))
orders_data = {}

for i in range(1, num_orders + 1):
    fio, pizza, amount = input(str(i + 1) + ' заказ :').split()
    amount = int(amount)
    if fio not in orders_data:
        orders_data[fio] = {pizza: amount}
    else:
        if pizza not in orders_data[fio]:
            orders_data[fio][pizza] = amount
        else:
            orders_data[fio][pizza] += amount

for fio, order in sorted(orders_data.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('\t', pizza, amount)

# order_count = int(input('Введите количество заказов: '))
# order_dict = dict()
#
# for order in range(order_count):
#     cur_order = input(f'{order + 1}-й заказ: ').title().split()
#     # cur_order[2] = int(cur_order[2])
#     if cur_order[0] not in order_dict:
#         order_dict[cur_order[0]] = {cur_order[1]: int(cur_order[2])}
#     else:
#         if cur_order[1] not in order_dict[cur_order[0]]:
#             order_dict[cur_order[0]][cur_order[1]] = int(cur_order[2])
#         else:
#             order_dict[cur_order[0]][cur_order[1]] += int(cur_order[2])
#
# print()
#
# for i_name, i_order in sorted(order_dict.items()):
#     print('{0}:'.format(i_name))
#     for i_pizza, i_count in sorted(i_order.items()):
#         print('\t\t{0}: {1}'.format(i_pizza, i_count))
#
