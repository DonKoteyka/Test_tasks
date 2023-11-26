import configparser
import pandas as pd
from line import get_line_new, get_line_1

config = configparser.ConfigParser()
config.read('config.ini')
base = config['base']
file_path = base['file_path']
lines = int(base['lines'])
max_tuples = int(base['max_tuples'])

data = pd.read_excel(file_path)

def test():
    for index in range(0, lines):

        # result = get_line_new(data, index, max_tuples)
        if index == 0:
            example = data.loc[136, f'Пролёт']
            result = get_line_1(data, index, max_tuples)

        else:
            example = data.loc[136, f'Пролёт.{index}']
            result = get_line_new(data, index, max_tuples)
        print()
        assert example-1 <= result <= example+1





