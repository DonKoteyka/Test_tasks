import csv

from service_csv.settings import MEDIA_ROOT


class ViewCSV:
    def __init__(self, name):
        self.name = name
        with open(MEDIA_ROOT + f'{self.name}.csv') as f:
            rows = csv.reader(f, delimiter=",")
            contacts_list = list(rows)
        self.content = contacts_list[1::]
        self.header = contacts_list[0]
