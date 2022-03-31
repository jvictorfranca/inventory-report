from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        splitted_path = path.split('.')
        extension = splitted_path[1]
        if extension != 'xml':
            raise(ValueError("Arquivo inválido"))
        with open(path) as fd:
            doc = xmltodict.parse(fd.read(), process_namespaces=True)
            data = [
                dict(obj)
                for obj in doc["dataset"]["record"]
              ]
        return data
