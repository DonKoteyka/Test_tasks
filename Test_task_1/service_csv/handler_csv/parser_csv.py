import csv

from service_csv.settings import MEDIA_ROOT


class ViewCSV:
    def __init__(self, file):
        self.file = file
        with open(MEDIA_ROOT + f'{self.file}') as f:
            rows = csv.reader(f, delimiter=",")
            contacts_list = list(rows)
        self.header = contacts_list[0]
        self.content = contacts_list[1::]
        self.id = str()
        self.created_at = str()

    def sort(self, sort):
        if sort:
            get_column = self.header.index(sort)
            self.content.sort(key=lambda x: x[get_column], reverse=True)
        else:
            pass

