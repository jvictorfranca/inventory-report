from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        splitted_path = path.split('.')
        extension = splitted_path[1]
        if extension != 'json':
            raise(ValueError("Arquivo inválido"))
        with open(path) as file:
            data = json.load(file)
            return data
