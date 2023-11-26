import pandas as pd

import configparser


config = configparser.ConfigParser()
config.read('config.ini')
base = config['base']
file_path = base['file_path']
lines = int(base['lines'])
max_tuples = int(base['max_tuples'])

def dict_count(data):
    if isinstance(data, dict):
        count = 0
        count += data.get('М', 0) * 15
        count += data.get('М2', 0) * 15
        count += data.get('З', 0) * 70

    elif isinstance(data, str):
        if data == 'М':
            count = 15
        elif data == 'З':
            count = 70
    return count


def get_line_new(data, index, max_tuples):
    dataset = data[[f'Опоры.{index}', f'Пролёт.{index}', f'Фидер.{index}', f'З/М.{index}', ]][0:max_tuples].dropna(
        subset=[f'Пролёт.{index}'])
    data_index = list(dataset.dropna(subset=[f'Фидер.{index}']).index)
    data_index += list(dataset.dropna(subset=[f'З/М.{index}']).index)
    data_index = sorted(list(set(data_index)))
    dataset[f'Фидер.{index}'] = dataset[f'Фидер.{index}'].ffill()
    count_line = list()
    count_line_extra = list()
    len_dataset = len(dataset)
    last_index = data_index[-1]
    for i, a in enumerate(data_index):
        if a == last_index and len_dataset - 1 != a:
            count_line.append(dataset.loc[a + 1:, f'Пролёт.{index}'])
            count_line_extra.append(dict_count(dict(dataset.loc[a + 1:, f'З/М.{index}'].value_counts())))
        elif a != last_index:
            b = data_index[i + 1] + 1

            count_line.append(dataset[a + 1:b][f'Пролёт.{index}'].replace('-', 0).sum())
            # if b > last_index:
            #     b = last_index
            count_line_extra.append(dict_count(dict(dataset.loc[a:b - 1, f'З/М.{index}'].value_counts())))
        else:
            count_line.append(0)
            count_line_extra.append(0)
    body = dataset.iloc[(data_index)]
    body[f"Длинна трассы на участке.{index}"] = count_line
    body[f"Дополнительный провод.{index}"] = count_line_extra
    body[f"Всего провода.{index}"] = (body[f"Длинна трассы на участке.{index}"].replace('-', 0) * 1.05).round() + body[
        f"Дополнительный провод.{index}"]
    res = body.drop([f'З/М.{index}', f'Пролёт.{index}', f'Дополнительный провод.{index}'], axis=1)
    res_total = res.transpose()

    xlsx_filename = f'результаты/схема/C_t_{index + 1}.xlsx'
    res_total.to_excel(xlsx_filename, index=False)

    summa = int(body[f"Всего провода.{index}"].sum())
    return summa


def get_line_1(data, index, max_tuples):
    dataset = data[[f'Опоры', f'Пролёт', f'Фидер', f'З/М', ]][0:max_tuples].dropna(
        subset=[f'Пролёт'])
    data_index = list(dataset.dropna(subset=[f'Фидер']).index)
    data_index += list(dataset.dropna(subset=[f'З/М']).index)
    data_index = sorted(list(set(data_index)))
    dataset[f'Фидер'] = dataset[f'Фидер'].ffill()
    count_line = list()
    count_line_extra = list()
    len_dataset = len(dataset)
    last_index = data_index[-1]
    for i, a in enumerate(data_index):
        if a == last_index and len_dataset - 1 != a:
            count_line.append(dataset.loc[a + 1:, f'Пролёт'])
            count_line_extra.append(dict_count(dict(dataset.loc[a + 1:, f'З/М'].value_counts())))
        elif a != last_index:
            b = data_index[i + 1] + 1
            count_line.append(dataset[a + 1:b][f'Пролёт'].replace('-', 0).sum())
            count_line_extra.append(dict_count(dict(dataset.loc[a:b - 1, f'З/М'].value_counts())))
        else:
            count_line.append(0)
            count_line_extra.append(0)
    body = dataset.iloc[(data_index)]
    body[f"Длинна трассы на участке"] = count_line
    body[f"Дополнительный провод"] = count_line_extra
    body[f"Всего провода"] = (body[f"Длинна трассы на участке"].replace('-', 0) * 1.05).round() + body[
        f"Дополнительный провод"]
    res = body.drop([f'З/М', f'Пролёт', f'Дополнительный провод'], axis=1)
    res_total = res.transpose()

    xlsx_filename = f'результаты/схема/C_t_{index + 1}.xlsx'
    res_total.to_excel(xlsx_filename, index=False)

    summa = int(body[f"Всего провода"].sum())
    return summa


if __name__ == "__main__":
    data = pd.read_excel(file_path)

    for i in range(6, lines):
        get_line_new(data, i, max_tuples)

    print('Выполнено!')
