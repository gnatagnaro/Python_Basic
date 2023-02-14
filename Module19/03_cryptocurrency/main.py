data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


# Вывести списки ключей и значений словаря.
print('1. Вывести списки ключей и значений словаря: ')
for i in data:
    print('{0}: {1}'.format(i, data.get(i)))
print()

# В “ETH” добавить ключ “total_diff” со значением 100.
print('2. В “ETH” добавить ключ “total_diff” со значением 100: ')
data.get('ETH').update({'total_diff': 100})
print(data.get('ETH'))
print()

# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
print('3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”: ')
data['tokens'][0]['fst_token_info']['name'] = 'doge'
print(data)
print()

# Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
print('4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”: ')
total_out = 0
for i in data['tokens']:
    total_out += i.pop('total_out')
data['ETH']['total_out'] = total_out
print(data)
print()

# Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
print('5. Внутри "sec_token_info" изменить название ключа “price” на “total_price”: ')
price = data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info'].update({'total_price': price})
print(data)
