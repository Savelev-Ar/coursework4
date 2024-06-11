import json
import os

class JSONSaver():
    """
    Класс для работы с файлом в формате json
    """
    def __init__(self, filename, list_vacancies):
        self.filename = filename
        self.list_vacancies = list_vacancies
    def add_vacancy(self, vacancy):
        self.list_vacancies.append(vacancy)
        self.save_file()

    def delete_vacancy(self, vacancy):
        self.list_vacancies.remove(vacancy)
        self.save_file()

    def save_file(self):
        """
        Метод для сохранения файла
        """
        if not os.path.isdir("data"):
            os.mkdir("data")
        with open(self.filename, 'w', encoding='utf-8') as file:
            list_ = []
            for vacancy in self.list_vacancies:
                dict_= {}
                dict_["name"] = vacancy.name
                dict_["salary_from"] = vacancy.salary_from
                dict_["salary_to"] = vacancy.salary_to
                dict_["url"] = vacancy.url
                dict_["requirements"] = vacancy.requirements
                list_.append(dict_)
            json.dump(list_, file, indent=4, ensure_ascii=False)

    def load_file_to_json(self):
        with (open(self.filename, encoding='utf-8') as file):
            data = json.load(file)
            self.list_vacancies = Vacancies.add_vacancies(data)

