from utils import *
from config import *
from hh import *
from vacancy import *
from fileworker import *


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий по запросу от пользователя
    hh_api = HHAPI()
    hh_api.load_vacancies(search_query)
    vacancies_list = Vacancies.add_vacancies(hh_api.vacancies)
    json_saver = JSONSaver(JSON_PATH, vacancies_list)
    json_saver.save_file()

    print(vacancies_list)

if __name__ == "__main__":
    user_interaction()