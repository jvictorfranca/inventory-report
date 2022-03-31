from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def get_aditional_string(self, list):
        initial_string = "Produtos estocados por empresa: \n"
        final_string = initial_string
        enterprises_list = [
          obj["nome_da_empresa"]
          for obj in list
        ]
        my_dict = {i: enterprises_list.count(i) for i in enterprises_list}
        for key in my_dict:
            final_string += f"- {key}: {my_dict[key]}\n"
        return final_string

    @classmethod
    def generate(self, list):
        data_antiga = self.get_older_date(list)
        data_validade = self.get_closer_date(list)
        nome_empresa = self.get_enterprise_with_most_sales(list)
        aditional_string = self.get_aditional_string(list)
        stringToReturn = f"Data de fabricação mais antiga: {data_antiga}\n" \
            f"Data de validade mais próxima: {data_validade}\n"\
            f"Empresa com maior quantidade de "\
            f"produtos estocados: {nome_empresa}\n\n"\
            f"{aditional_string}"
        return stringToReturn
