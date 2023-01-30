print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

# y1 = k * x1 + b -> k = (y1 - b) / x1
# y2 = k * x2 + b

x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print(f'Уравнение вида y = k * x + b составить нельзя, так как данное уравнение прямой x = {x1}')
else:
    k = y_diff / x_diff
if k == 0:
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y =", b)
else:
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y =", k, "* x +", b)