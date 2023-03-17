class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child_list = []

    def print_info(self):
        print('Родитель:')
        print(f'Имя: {self.name}, Возраст: {self.age}')
        print('Список детей: ')
        for child in self.child_list:
            print(f'Ребенок {child.name}, '
                  f'возраст: {child.age}, '
                  f'состояние спокойствия: {child.calm_state}, '
                  f'состояние голода: {child.hunger_state}')

    def calm_child(self, child):
        if not child.calm_state:
            child.calm_state = True

    def feed_child(self, child):
        if child.hunger_state:
            child.hunger_state = False


class Child:

    def __init__(self, name, age, parent, calm_state=True, hunger_state=False):
        self.name = name
        if parent.age >= age + 16:
            self.age = age
            self.calm_state = calm_state
            self.hunger_state = hunger_state
            parent.child_list.append(self)
        else:
            self.res = f'{parent.name} слишком молод, чтобы быть родителем {self.name}'


Tom = Parent('Том', 16)
Fred = Child('Фрэд', 15, Tom)
print(Fred.res)
x = Parent('123', 50)
Fred = Child('f', 15, x)
print(x.child_list[0].name)
x.print_info()
