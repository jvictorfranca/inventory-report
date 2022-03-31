import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class DataReader():
    @classmethod
    def read_csv(cls, path):
        with open(path) as file_object:
            data = csv.DictReader(file_object)
            answer = [object for object in data]
            return answer

    @classmethod
    def read_xml(cls, path):

        with open(path) as fd:
            doc = xmltodict.parse(fd.read(), process_namespaces=True)
            data = [
                dict(obj)
                for obj in doc["dataset"]["record"]
              ]
        return data

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            data = json.load(file)
            return data

    @classmethod
    def get_extension(cls, path):
        splitted_path = path.split('.')
        extension = splitted_path[1]
        return extension

    @classmethod
    def read_data(cls, path):
        extension = cls.get_extension(path)
        if extension == 'json':
            data = cls.read_json(path)
        elif extension == 'csv':
            data = cls.read_csv(path)
        elif extension == 'xml':
            data = cls.read_xml(path)
        else:
            raise(Exception(ValueError))
        return data


class Inventory():
    @classmethod
    def import_data(cls, path, tipo):
        data = DataReader.read_data(path)
        if tipo == "simples":
            dataToReturn = SimpleReport.generate(data)
        elif tipo == "completo":
            dataToReturn = CompleteReport.generate(data)
        return dataToReturn
