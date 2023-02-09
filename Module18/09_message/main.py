message = input('Сообщение: ').split()
new_message = []

for i in message:
    part1 = ''
    part2 = ''

    for j in i:
        if j.isalpha():
            part1 += ''.join([j])
        else:
            part2 += ''.join(reversed(part1)) + j
            part1 = ''

    part2 += ''.join(reversed(part1))
    new_message.append(part2)

print('Новое сообщение: {}'.format(' '.join(new_message)))



