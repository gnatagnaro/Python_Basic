import re


if __name__ == '__main__':

    text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
    nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
    Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
    """

    pattern = re.compile(r'\b\w{4}\b')
    pattern = re.compile(r'\b\w{4}\b')
    # pattern = re.compile(r'\b\w\w\w\w\b') #  так тоже можно
    print(pattern.findall(text))
