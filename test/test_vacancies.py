import pytest
from src.vacancies import Vacancies

@pytest.fixture
def vacancies():
    return Vacancies("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
                   4_000_000, 7_000_000, "Ташкент",
                   "Опыт работы в продажах обязателен", "Консультирование клиентов")


@pytest.fixture()
def vacancies2():
    return Vacancies("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
                   40_000, 70_000, "Ташкент",
                   "Опыт работы в продажах обязателен", "Консультирование клиентов")


def test_vacancies_init(vacancies):
    """ Тесты конструктора класса """

    assert vacancies.name == "Менеджер по работе с клиентами"
    assert vacancies.alternate_url == "https://hh.ru/vacancy/101709979"
    assert vacancies.salary_from == 4_000_000
    assert vacancies.salary_to == 7_000_000
    assert vacancies.area_name == "Ташкент"
    assert vacancies.requirement == "Опыт работы в продажах обязателен"
    assert vacancies.responsibility == "Консультирование клиентов"


def test_vacancies_str(vacancies):
    """ Тест строкового представления вакансии """

    assert str(vacancies) == ("Наименование вакансии: Менеджер по работе с клиентами\n"
                            "Ссылка на вакансию: https://hh.ru/vacancy/101709979\n"
                            "Зарплата: от 4000000 до 7000000\n"
                            "Место работы: Ташкент\n"
                            "Краткое описание: Опыт работы в продажах обязателен\n"
                            "Консультирование клиентов\n")


def test_vacancies_lt(vacancies, vacancies2):
    """ Тест утверждает, что одно значение меньше другого """

    assert vacancies2 < vacancies
    if vacancies > vacancies2:
        assert ValueError


def test_vacancies_from_hh_dict(vacancies):
    """ Тест утверждает, что метод вернет экземпляр класса в виде списка """

    assert (
        "Наименование вакансии: Менеджер по работе с клиентами,"
        "Ссылка на вакансию: https://hh.ru/vacancy/101709979,"
        "Зарплата: от 4000000 до 7000000,"
        "Место работы: Ташкент,"
        "Краткое описание: Опыт работы в продажах обязателен,"
        "Консультирование клиентов,"
    )


def test_vacancies_to_dict(vacancies):
    """ Тест утверждает, что метод вернет вакансию в виде словаря """

    assert {
        "name": "Менеджер по работе с клиентами",
        "alternate_url": "https://hh.ru/vacancy/101709979",
        "salary_from": 4000000,
        "salary_to": 7000000,
        "area_name": "Ташкент",
        "requirement": "Опыт работы в продажах обязателен",
        "responsibility": "Консультирование клиентов"
    }