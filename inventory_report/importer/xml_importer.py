import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def read_file_path(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as f:
            data = f.read()
            result_data = xmltodict.parse(data)["dataset"]["record"]
        return result_data
