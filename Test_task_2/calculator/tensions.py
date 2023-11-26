import pandas as pd
from main import file_path, lines, max_tuples


# file_path = 'Расчёты_2.xlsx'
# data = pd.read_excel(file_path)


def handle_excel(data, index, max_tuples):

    b = '''Тип крепления кабеля где А - натяжное анкерное, П - промежуточное поддерживающее. Можно вводить также 
    прописные а и п'''
    c = '''Высота подвеса кабеля, м введите высоту подвеса кабеля в метрах'''
    d = '''Пролёт между опорами'''
    e = '''Длина пролёта, м введите длину пролёта между опорами в метрах'''
    if index != 0:
        len_line = len(data[f'Опоры.{index}'][0:max_tuples].dropna())
        get_length_line = list(data[f'Пролёт.{index}'][1:len_line])
        get_length_line.append('')
        get_types = list(data[f'А/П.{index}'][0:len_line])
    else:
        len_line = len(data['Опоры'][0:max_tuples].dropna())
        get_length_line = list(data['Пролёт'][1:len_line])
        get_length_line.append('')
        get_types = list(data['А/П'][0:len_line])
    data_to_exit = {
        'Номер опоры': range(len_line),
        b: get_types,
        c: [6 for _ in range(len_line)],
        d: list(f'{i}-{i+1}' for i in range(len_line)),
        e: get_length_line
    }
    result = pd.DataFrame(data_to_exit)

    xlsx_filename = f'результаты/Л_{index+1}.xlsx'
    result.to_excel(xlsx_filename, index=False)


if __name__ == "__main__":
    # file_path = input('Введите имя файла: ')
    # lines = int(input('Введите количество линий: '))

    data = pd.read_excel(file_path)
    for i in range(lines):
        handle_excel(data, i, max_tuples)
    print('Выполнено!')

