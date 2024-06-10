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
            if vacancy.get('salary') != None and vacancy.get('salary').get('currency') == 'RUR':
                if vacancy.get('salary').get('from') != None or vacancy.get('salary').get('to') != None:
                    if vacancy.get('salary')['from'] != None:
                        salary_from = vacancy.get('salary')['from']
                    else:
                        salary_from = 0
                    if vacancy.get('salary')['to'] != None:
                        salary_to = vacancy.get('salary')['to']
                    else:
                        salary_to = 0
                    if vacancy.get('snippet').get('requirement') != None:
                        requirement = vacancy.get('snippet').get('requirement').replace('<highlighttext>','').replace('</highlighttext>','')
                    result.append(Vacancies(vacancy.get('name'), salary_from, salary_to,
                                            requirement,
                                            vacancy.get('alternate_url')))
        return result

    def __lt__(self, other):
        self_ = int(self.salary_from)
        other_ = int(other.salary_from)
        if self_ != 0 or other_ != 0:
            return self_ < other_
        else:
            return int(self.salary_to) < int(other.salary_to)
    def __repr__(self):
        return (f'Вакансия : {self.name} ,'
                f' зарплата: от {self.salary_from} до {self.salary_to},'
                f' ссылка : {self.url} ,'
                f' требования : {self.requirements} \n')
