from utils import *
from config import *
from hh import *

# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HHAPI()
    hh_api.load_vacancies(search_query)

    print(hh_api.vacancies)


if __name__ == "__main__":
    user_interaction()