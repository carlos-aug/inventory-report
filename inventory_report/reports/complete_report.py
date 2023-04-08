from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):

        result_products = {}

        for index in list:
            if index["nome_da_empresa"] in result_products:
                result_products[index["nome_da_empresa"]] += 1
            else:
                result_products[index["nome_da_empresa"]] = 1
        stock = "\nProdutos estocados por empresa:\n"
        for key, value in result_products.items():
            stock += f"- {key}: {value}\n"
        return SimpleReport.generate(list) + stock
