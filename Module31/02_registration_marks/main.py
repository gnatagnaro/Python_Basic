import re


if __name__ == '__main__':

    text = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'"
    private_cars_pattern = re.compile(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}')
    taxis_pattern = re.compile(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}')

    print(f'Список номеров частных автомобилей: {private_cars_pattern.findall(text)}')
    print(f'Список номеров такси: {taxis_pattern.findall(text)}')
