from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def read_file_path(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as f:
            data = ET.parse(f)
            return data
