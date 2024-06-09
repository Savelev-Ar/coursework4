class Vacancies():

    def __init__(self, name, salary_from, salary_to, requirements, url):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements
        self.url = url

    @classmethod
    def add_vacancies(cls, vacancies_list):
        result = []
        for vacancy in vacancies_list:
            if vacancy.get('salary') != None:
                if vacancy.get('salary').get('from') != None or vacancy.get('salary').get('to') != None:
                    if vacancy.get('salary')['from'] != None:
                        salary_from = vacancy.get('salary')['from']
                    else:
                        salary_from = 0
                    if vacancy.get('salary')['to'] != None:
                        salary_to = vacancy.get('salary')['to']
                    else:
                        salary_to = 0
                    result.append(Vacancies(vacancy.get('name'), salary_from, salary_to, vacancy.get('snippet').get('requirement'),  vacancy.get('alternate_url')))
        return result

    def __lt__(self, other):
        if self.salary_from != 0 and other.salary_from != 0:
            return self.salary_from < other.salary_from
        else:
            return self.salary_to < other.salary_to
    def __repr__(self):
        return f'Вакансия: {self.name} , зарплата от {self.salary_from} до {self.salary_to}, ссылка: {self.url} , требования: {self.requirements}\n'
