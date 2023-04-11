from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def read_file_path(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path, "r") as f:
            data = list(csv.DictReader(f))
            return data
