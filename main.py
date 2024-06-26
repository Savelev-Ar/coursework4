from src.utils import top_vacancies, filtered_vacancies
from config import JSON_PATH
from src.vacancy import Vacancies
from src.fileworker import JSONSaver
from src.hh import HHAPI


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий  по запросу от пользователя
    hh_api = HHAPI()
    hh_api.load_vacancies(search_query)
    vacancies_list = Vacancies.add_vacancies(hh_api.vacancies)

    # Сохранение полученных вакансий в файл
    json_saver = JSONSaver(JSON_PATH, vacancies_list)
    json_saver.save_file()

    user_filter = input("Введите слова для фильтрации вакансий: ")
    # Фильтрация вакансий
    filtered_vacancies(vacancies_list, user_filter)

    user_top = int(input("Введите количество вакансий в топе: "))
    # Вывод топа вакансий
    print(top_vacancies(vacancies_list, user_top))


if __name__ == "__main__":
    user_interaction()