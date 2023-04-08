from datetime import date


class SimpleReport:
    @staticmethod
    def old_manufacture(list):
        result_old_manufacture = []

        for index in list:
            result_old_manufacture.append(index["data_de_fabricacao"])
        return min(result_old_manufacture)

    def closest_expiration(list):
        date_today = date.today().isoformat()
        result_date = []

        for index in list:
            if index["data_de_validade"] >= date_today:
                result_date.append(index["data_de_validade"])
        return min(result_date)

    def company_with_the_most_products(
        list,
    ):
        result_products = {}

        for index in list:
            if index["nome_da_empresa"] in result_products:
                result_products[index["nome_da_empresa"]] += 1
            else:
                result_products[index["nome_da_empresa"]] = 1
        return max(result_products, key=result_products.get)

    @staticmethod
    def generate(list):
        old_manufacture = SimpleReport.old_manufacture(list)
        closest_expiration = SimpleReport.closest_expiration(list)
        company_with_the_most_products = (
            SimpleReport.company_with_the_most_products(list)
        )

        return (
            f"Data de fabricação mais antiga: { old_manufacture }\n"
            f"Data de validade mais próxima: { closest_expiration }\n"
            f"Empresa com mais produtos: { company_with_the_most_products }"
        )
