def is_palindrome(num_list):
    reverse_list = []
    for el in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[el])
    if reverse_list == num_list:
        return True
    else:
        return False


nums = []
n = int(input('Кол-во чисел: '))
for i in range(n):
    x = int(input(f'Введите {i + 1} элемент последовательности: '))
    nums.append(x)

answer = []
for i in range(0, len(nums)):
    new_nums = []
    for j in range(i, len(nums)):
        new_nums.append(nums[j])
    if is_palindrome(new_nums):
        for ans in range(0, i):
            answer.append(nums[ans])
        answer.reverse()
        break

print(f'Последовательность: {nums}')
print(f'Нужно приписать чисел: {len(answer)}')
print(f'Сами числа: {answer}')
