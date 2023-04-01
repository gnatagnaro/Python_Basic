import re


if __name__ == '__main__':

    phone_numbers = ['9999999999', '999999-999', '99999x9999']
    # так тоже работает:
    # pattern_number = re.compile(r'[8-9]\d{9}')
    # но лучше так:
    pattern_number = re.compile(r'^[8-9]\d{9}$')

    for number in phone_numbers:
        if re.match(pattern_number, number):
            print(f'{number}: все в порядке')
        else:
            print(f'{number}: не подходит')

