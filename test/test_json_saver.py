import pytest
import os
from src.json_saver import JSONSaver

VACANCIES_PATH_JSON = os.path.join(os.path.dirname(__file__), "../data", "vacancies.json")

@pytest.fixture()
def json_saver():
    return JSONSaver(filename=VACANCIES_PATH_JSON)

def test_write_data(json_saver):
    json_saver.write_data(
        [
            {
                "name": "Медсестра/медбрат универсал на Фурманова 220/3",
                "alternate_url": "https://hh.ru/vacancy/104213899",
                "salary_from": 228550,
                "salary_to": 285688,
                "area_name": "Алматы",
                "requirement": "Средне-специальное медицинское образование. Опыт работы желателен. "
                               "Наличие действующего сертификата специалиста. Опытный пользователь ПК.",
                "responsibility": "Хранение и подготовка к транспортировке биоматериала. "
                                  "Соблюдение санэпидрежима, правил асептики и антисептики. "
                                  "Сервисное поведение. Регистрация пациентов и консультирование "
                                  "(совмещение <highlighttext>админ</highlighttext>..."
            }
        ]
    )


def test_get_data(json_saver):
    assert len(json_saver.get_data()) >0


def test_del_data(json_saver):
    assert json_saver.del_data() is None