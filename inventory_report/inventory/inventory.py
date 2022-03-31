import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    @classmethod
    def read_data(cls, path):
        with open(path) as file_object:
            data = csv.DictReader(file_object)
            return [object for object in data]

    @classmethod
    def import_data(cls, path, tipo):
        data = cls.read_data(path)
        if tipo == "simples":
            dataToReturn = SimpleReport.generate(data)
        elif tipo == "completo":
            dataToReturn = CompleteReport.generate(data)
        return dataToReturn
