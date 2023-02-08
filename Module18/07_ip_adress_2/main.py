# ip_address = "{0}.{1}.{2}.{3}"
# count = 0
# numbers = []
# while count < 4:
#     new_number = int(input("Введите число: "))
#     if 0 <= new_number <= 255:
#         numbers.append(new_number)
#         count += 1
#
# print(ip_address.format(*numbers))

ip_address = "{0}.{1}.{2}.{3}"
count = 0
new_ip = input('Введите IP: ').split('.')
# print(new_ip)
if len(new_ip) == 4:
    for i in range(len(new_ip)):
        count += 1
        if new_ip[i].isdigit():
            if (0 <= int(new_ip[i]) <= 255) and count == 4:
                print('IP-адрес корректен.')
            elif (0 <= int(new_ip[i]) <= 255) and count < 4:
                continue
            else:
                print(f'{new_ip[i]} превышает 255.')
        else:
            print(f'{new_ip[i]} — это не целое число.')
else:
    print('Адрес — это четыре числа, разделённые точками.')
# print(ip_address.format(*new_ip))
