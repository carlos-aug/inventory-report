from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def read_file_path(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data
