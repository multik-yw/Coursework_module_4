import os
from src.api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy

VACANCIES_PATH_JSON = os.path.join(os.path.dirname(__file__), "../data", "vacancies.json")

def user_choice_json():
    """Функция для работы с пользователем, записи в json-файл"""

    keyword = input("Какую профессию ищите?\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    saver = JSONSaver(VACANCIES_PATH_JSON)

    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в json-файл")