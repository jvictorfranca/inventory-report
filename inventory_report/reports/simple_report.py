import datetime


class SimpleReport():
    @classmethod
    def get_older_date(self, list):
        all_dates = [
            obj["data_de_fabricacao"]
            for obj in list
        ]

        date = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in all_dates]
        date.sort()
        sorted = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in date]
        return sorted[0]

    @classmethod
    def get_closer_date(self, list):
        all_dates = [
            obj["data_de_validade"]
            for obj in list
        ]

        date = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in all_dates]
        min_date = min(date, key=lambda x: abs(x - datetime.datetime.today()))
        min_string = datetime.datetime.strftime(min_date, "%Y-%m-%d")
        return min_string

    @classmethod
    def get_enterprise_with_most_sales(self, list):
        enterprises_list = [
          obj["nome_da_empresa"]
          for obj in list
        ]

        my_dict = {i: enterprises_list.count(i) for i in enterprises_list}
        max_value = max(my_dict, key=my_dict.get)
        return max_value

    @classmethod
    def generate(self, list):
        data_antiga = self.get_older_date(list)
        data_validade = self.get_closer_date(list)
        nome_empresa = self.get_enterprise_with_most_sales(list)
        stringToReturn = f"Data de fabricação mais antiga: {data_antiga}\n" \
            f"Data de validade mais próxima: {data_validade}\n"\
            f"Empresa com maior quantidade de "\
            f"produtos estocados: {nome_empresa}\n"
        print(stringToReturn)
        return stringToReturn
