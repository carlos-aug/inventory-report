from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type_report):
        result_data = Inventory.read_file_path(path)
        if type_report == "simples":
            return SimpleReport.generate(result_data)
        elif type_report == "completo":
            return CompleteReport.generate(result_data)

    def read_file_path(path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)
