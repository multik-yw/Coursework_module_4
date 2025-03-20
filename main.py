from src.json_saver import JSONSaver
from src.utils import user_choice_json

import os

VACANCIES_PATH_JSON = os.path.join(os.path.dirname(__file__), "../data", "vacancies.json")

def main():
    """Запуск программы"""
    user_input = input("Здравствуйте!\n"
                       "Если вы хотите записать данные в файл, введите 1\n"
                       "Если хотите удалить данные из файла, введите 2\n")

    if user_input == "1":
        user_choice_json()
    elif user_input == "2":
        deleter = JSONSaver(VACANCIES_PATH_JSON)
        deleter.del_data()
        print("Данные удалены!")
    return


if __name__ == "__main__":
    main()