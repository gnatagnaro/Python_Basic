numbers_sum = 0
file_from = open("numbers.txt", "r", encoding="utf-8")
for line in file_from:
    clear_line = line.strip()
    if clear_line:
        numbers_sum += int(clear_line)
file_from.close()

file_in = open("answer.txt", "a", encoding="utf8")
file_in.write(str(numbers_sum) + '\n')
file_in.close()
