import os
import os.path as path
import csv
import json


def convert_bytes(size):
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return str(size) + " " + x
        else:
            size /= 1024.0


def get_files_sizes(dirpath):
    file_arr = os.listdir(dirpath)
    for filename in file_arr:
        print(str(filename) + ':', convert_bytes(path.getsize(dirpath + '/' + filename)))


myPath = 'C://temp/test/'
get_files_sizes(myPath)

csv_filename = input("Введите название csv-файла: ")

try:
    with open(myPath + csv_filename, encoding='utf-8') as csv_f:
        reader = csv.DictReader(csv_f)
        result = []
        result1 = []
        for row in reader:
            row['n'] = int(row['n'])
            result.append(row)
        for row in result:
            print(row)

        print("Сортировка по ФИО:")
        result.sort(key=lambda r: r['fio'])
        for row in result:
            print(row)

        print("Сортировка по номеру посещения:")
        result.sort(key=lambda r: r['n'])
        for row in result:
            print(row)
        print("Строки с критерием type = ""Выписка"":")
        for row in result:
            if row.get('type') == "Выписка":
                result1.append(row)
                print(row)
        with open(myPath + 'result.json', 'w') as res:
            res.write(json.dumps(result1, ensure_ascii=False))
            res.close()
        csv_f.close()
        os.replace(myPath + 'result.json', path.dirname(path.dirname(myPath)) + '/result.json')
        #os.remove(myPath + csv_filename)
except FileNotFoundError:
    print("Ошибка: файл не найден")
except NotImplementedError:
    print("Ошибка: ключ не найден")

