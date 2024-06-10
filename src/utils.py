def filtered_vacancies(vacancies_list, user_filter):
    for vacancy in vacancies_list:
        if str(vacancy).find(user_filter) == -1:
            vacancies_list.remove(vacancy)

def top_vacancies(vacancies_list, n):
    sorted_list = sorted(vacancies_list, reverse=True)
    return sorted_list[0:n+1]

