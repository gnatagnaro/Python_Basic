def synonym_dict(dict):
    word = input('Введите слово: ').title()
    for i in dict.keys():
        if word in dict[i]:
            if word == dict[i][0]:
                print('Синоним: {}'.format(dict[i][1]))
                break
            else:
                print('Синоним: {}'.format(dict[i][0]))
                break
    else:
        print('Такого слова в словаре нет.')
        synonym_dict(dict)


count_pairs = int(input('Введите количество пар слов: '))
pairs_dict = dict()

for pair in range(count_pairs):
    cur_pair = input('{x}-ая пара: '.format(x=pair+1)).title().split(' - ')
    pairs_dict[pair] = cur_pair

synonym_dict(pairs_dict)

