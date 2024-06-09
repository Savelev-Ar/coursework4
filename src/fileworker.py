import json

class JSONSaver():

    def __init__(self, filename, list_vacancies):
        self.filename = filename
        self.list_vacancies = list_vacancies
    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass

    def save_file(self):
        with (open(self.filename, 'w', encoding='utf-8') as file):
            for vacancy in self.list_vacancies:
                dict_= {}
                dict_["name"] = vacancy.name
                dict_["salary_from"] = vacancy.salary_from
                dict_["salary_to"] = vacancy.salary_to
                dict_["url"] = vacancy.url
                dict_["requirements"] = vacancy.requirements
                json.dump(dict_, file, indent=4, ensure_ascii=False)

    def load_file_to_json(self):
        pass
