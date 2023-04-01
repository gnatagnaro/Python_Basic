import requests
import json


if __name__ == '__main__':
    # Получаем информацию о корабле Millennium Falcon
    ship_name = "Millennium Falcon"
    ship_url = f"https://swapi.dev/api/starships/?search={ship_name}"
    response = requests.get(ship_url)

    # data = response.json()["results"][0]
    data = json.loads(response.text)['results'][0]

    # Извлекаем интересующие нас данные
    ship = {
        "name": data["name"],
        "max_speed": data["max_atmosphering_speed"],
        "class": data["starship_class"],
        "pilots": []
    }

    # Получаем список пилотов корабля
    for url in data["pilots"]:
        response = requests.get(url)
        # data = response.json()
        data = json.loads(response.text)

        # Получаем информацию о родной планете каждого пилота
        planet_url = data["homeworld"]
        response = requests.get(planet_url)
        # planet_data = response.json()
        planet_data = json.loads(response.text)

        # Извлекаем интересующие нас данные о пилоте и его родной планете
        pilot = {
            "name": data["name"],
            "height": data["height"],
            "mass": data["mass"],
            "homeworld": planet_data["name"],
            "homeworld_info": planet_data["url"]
        }

        # Добавляем пилота в список
        ship["pilots"].append(pilot)

    # Выводим результаты в консоль
    print("Ship name:", ship["name"])
    print("Max speed:", ship["max_speed"])
    print("Class:", ship["class"])
    print("")

    print("Pilots:")
    for pilot in ship["pilots"]:
        print("Name:", pilot["name"])
        print("Height:", pilot["height"])
        print("Mass:", pilot["mass"])
        print("Homeworld:", pilot["homeworld"])
        print("Homeworld info:", pilot["homeworld_info"])
        print("")

    # Записываем результаты в файл в формате JSON
    with open("millennium_falcon_info.json", "w") as f:
        json.dump(ship, f, indent=4)
