import random

POTATO_SEED = 0
POTATO_GREEN = 1
POTATO_NEW = 2
POTATO_FULLY_FLEDGED = 3

STATUSES = {
    POTATO_SEED: 'посеянная',
    POTATO_GREEN: 'зеленая ботва',
    POTATO_NEW: 'молодая',
    POTATO_FULLY_FLEDGED: 'зрелая',
    }

HILL_UP_PROBABILITY = 0.5
FREE_GROW_PROBABILITY = 0.1
SPUD_GROW_PROBABILITY = 0.8
HARVESTING_FULLY_FLEDGED = 0.8


class Potato:
    def __init__(self, index, patch):
        self.index = index
        self.patch = patch
        self.ripe = POTATO_SEED

    def grow(self):
        self.ripe += 1
        self.ripe = min(self.ripe, POTATO_FULLY_FLEDGED)

    def get_status(self):
        return self.ripe

    def get_status_str(self):
        return ' '.join(['Картошка', str(self.index), STATUSES[self.ripe]])


class PotatoPatch:
    def __init__(self, potatoes_qty):
        self.potatoes = [Potato(i, self) for i in range(potatoes_qty)]

    def grow(self, probs=None):
        for potato in self.potatoes:
            if probs is None:
                potato.grow()
            elif potato.index > len(probs):
                potato.grow()
            elif probs[potato.index]:
                potato.grow()

    def get_status(self):
        statuses = []
        for potato in self.potatoes:
            statuses.append(potato.get_status())
        return statuses

    def get_status_str(self):
        statuses = []
        for potato in self.potatoes:
            statuses.append(potato.get_status_str())
        return statuses


class Gardener:
    def __init__(self, patch, name):
        self.name = name
        self.patch = patch

    def is_hill_up(self):
        return random.random() < HILL_UP_PROBABILITY

    def growing(self):
        spud_probs = [random.random() for _ in self.patch.potatoes]
        hill_up = False
        if self.is_hill_up():
            hill_up = True
            spud_probs = [prob < SPUD_GROW_PROBABILITY for prob in spud_probs]
        else:
            spud_probs = [prob < FREE_GROW_PROBABILITY for prob in spud_probs]

        self.patch.grow(spud_probs)

        return hill_up


def is_harvesting(patch):
    potatoes_threshold = int(HARVESTING_FULLY_FLEDGED * len(patch.potatoes))
    summ = get_fully_fledged_potatoes_qty(patch)
    
    return summ >= potatoes_threshold


def get_fully_fledged_potatoes_qty(patch):
    summ = 0
    for status in patch.get_status():
        summ += int(status == POTATO_FULLY_FLEDGED)
    return summ


def main():
    potatoes_qty = 5

    patch = PotatoPatch(potatoes_qty)
    name = input('Введите ваше имя: ')
    gardener = Gardener(patch, name)

    harvesting = False
    week = 1
    while not harvesting:
        print(f'неделя {week}')
        print(f'Наш садовник - {gardener.name} обходит свой огород')
        hill_up = gardener.growing()
        if hill_up:
            print(f'На этой неделе он активно работал и прополол грядку')
        else:
            print(f'На этой неделе он ленился')
        
        print('Результатом его работы стало:')
        
        for status_str in patch.get_status_str():
            print(status_str)
        
        harvesting = is_harvesting(patch)
        week += 1

    print('Урожай поспел')
    fledged_potatoes = get_fully_fledged_potatoes_qty(patch)
    print(f'Наш садовник - {gardener.name} собрал {fledged_potatoes} картошек')


main()
