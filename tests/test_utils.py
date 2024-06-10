from src.utils import *
from src.vacancy import *

vacancies_list = Vacancies.add_vacancies([])

def test_filtered_vacancies():
    assert filtered_vacancies(vacancies_list, '') == ''

def test_top_vacancies():
    top_vacancies(vacancies_list, 0) == ''

