from pandas import DataFrame

from line import get_line_new, get_line_1
from tensions import handle_excel
from progress.bar import Bar

import pandas as pd
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
base = config['base']
file_path = base['file_path']
lines = int(base['lines'])
max_tuples = int(base['max_tuples'])


if __name__ == "__main__":

    
    data: DataFrame = pd.read_excel(file_path)
    bar = Bar('Processing', max=lines)

    for i in range(lines):
        bar.next()
        if i == 0:
            get_line_1(data, i, max_tuples)
        else:
            get_line_new(data, i, max_tuples)
        handle_excel(data, i, max_tuples)
    bar.finish()
    print('Выполнено!')
