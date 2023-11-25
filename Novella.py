def start_game():
    print("Добро пожаловать в игру Новелла с сюжетом из Формаж 3!")
    print("Введите 'start', чтобы начать игру:")
    choice = input()

    if choice == "start":
        character_selection()
    else:
        print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        start_game()


def character_selection():
    print("Выберете своего персонажа:")
    print("1. Герой")
    print("2. Злодей")
    choice = input()

    if choice == "1":
        character_name = "Герой"
    elif choice == "2":
        character_name = "Злодей"
    else:
        print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        character_selection()

    print(f"Вы выбрали персонажа {character_name}.")
    play_game(character_name)


def play_game(character_name):
    print(f"Вы играете за {character_name}.")
    print("Введите 'вперед', чтобы продолжить:")
    choice = input()

    if choice == "вперед":
        print("Вы идете вперед и встречаете загадочную фигуру.")
        mystery_figure()
    else:
        print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        play_game(character_name)


def mystery_figure():
    print("Загадочная фигура предлагает вам сделать выбор:")
    print("1. Присоединиться к ней")
    print("2. Проигнорировать и продолжить свой путь")
    choice = input()

    if choice == "1":
        print("Вы присоединяетесь к загадочной фигуре, и она открывает перед вами тайную дверь.")
        secret_door()
    elif choice == "2":
        print("Вы проигнорировали загадочную фигуру и продолжаете свой путь.")
        continue_journey()
    else:
        print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        mystery_figure()


def secret_door():
    print("Вы входите в тайную дверь и оказываетесь в комнате сокровищ.")
    print("1. Взять все сокровища")
    print("2. Взять только часть сокровищ")
    choice = input()

    if choice == "1":
        print("Вы берете все сокровища и становитесь богатым!")
        end_game()
    elif choice == "2":
        print("Вы берете только часть сокровищ и продолжаете свой путь.")
        continue_journey()
    else:
        print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        secret_door()


def continue_journey():
    print("Вы продолжаете свой путь и встречаете новые приключения...")
    end_game()


def end_game():
    print("Игра окончена. Спасибо за игру!")
    print("Хотите сыграть еще раз? (Да/Нет)")
    choice = input()

    if choice.lower() == "да":
        start_game()
    elif choice.lower() == "нет":
        print("До свидания!")
    else:
        print("Некорректный выбор. Игра окончена.")


start_game()