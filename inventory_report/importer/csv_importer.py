from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        splitted_path = path.split('.')
        extension = splitted_path[1]
        if extension != 'csv':
            raise(ValueError("Arquivo inválido"))
        with open(path) as file_object:
            data = csv.DictReader(file_object)
            answer = [object for object in data]
            return answer
