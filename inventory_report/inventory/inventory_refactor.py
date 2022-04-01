from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, tipo):
        self.data += self.importer.import_data(path)
        if tipo == "simples":
            dataToReturn = SimpleReport.generate(self.data)
            print(dataToReturn)
        elif tipo == "completo":
            dataToReturn = CompleteReport.generate(self.data)
        return dataToReturn

    def __iter__(self):
        return InventoryIterator(self.data)
