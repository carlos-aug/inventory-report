import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path, "r") as f:
            data = list(csv.DictReader(f))
            return data
