import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    path = sys.argv[1]
    type = sys.argv[2]

    importer = CsvImporter
    splitted_path = path.split('.')
    extension = splitted_path[1]

    if extension == 'json':
        importer = JsonImporter

    if extension == 'xml':
        importer = XmlImporter
 
    instancia = InventoryRefactor(importer)
    report = instancia.import_data(path, type)
    print(report, end='')
