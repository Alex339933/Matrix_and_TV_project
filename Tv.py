# Эта функция ищет шоу по жанру


def search_genre(genre):
    found_serials = []
    for serial in serials_db:
        if serial["genre"] == genre:
            found_serials.append(serial)
    return found_serials


def print_dict(data: dict):
    print('=' * 20)
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

# Эта функция ищет шоу по рейтингу


def search_rating(rating):
    found_serials = []
    for serial in serials_db:
        if serial["rating"] == rating:
            found_serials.append(serial)
    return found_serials


# Эта функция выводит информацию про все шоу

def display_all():
    print("Список всех шоу: ")
    for line in serials_db:
        print_dict(line)
    print('=' * 20)


if __name__ == "__main__":
    serials_db = [{"title": "Chronicles of the Galaxy", "genre": "Adventure", "seasons": 5, "rating": 8},
                  {"title": "Mystery Island", "genre": "Fantasy", "seasons": 3, "rating": 9},
                  {"title": "Epic Quest", "genre": "Fantasy", "seasons": 4, "rating": 7},
                  {"title": "Crime Files", "genre": "Crime Drama", "seasons": 6, "rating": 5},
                  {"title": "Medical Miracles", "genre": "Medical Drama", "seasons": 2, "rating": 8},
                  {"title": "Time Travelers", "genre": "Adventure", "seasons": 4, "rating": 8},
                  {"title": "Comedy Central", "genre": "Comedy", "seasons": 7, "rating": 9}]
    print("Выберите опции: ")
    print("1 - Искать шоу по жанру, 2 - Искать шоу по рейтингу, 3 - Информация о всех шоу")
    user_input = input()
    if user_input == "1":
        user_genre = input("Введите нужный жанр: ")
        results = search_genre(user_genre)
        if results:
            print(f"Найдено {len(results)}!")
            for result in results:
                print_dict(result)
        else:
            print("Нет такого жанра у шоооу!")
    elif user_input == "2":
        user_rating = int(input("Введите нужный рейтинг: "))
        results = search_rating(user_rating)
        if results:
            print(f"Найдено {len(results)}!")
            for result in results:
                print_dict(result)
        else:
            print("Нет такого рейтинга у шоооу!")
    elif user_input == "3":
        display_all()
    else:
        print("Такого действия нет")


