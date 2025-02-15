import json
import argparse
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bot import nspd_bot
from config import fields


def parse_egrn_data(text):
    """
    Парсит текст, полученный с сайта, и возвращает словарь с результатами.
    """
    data = {}
    if 'Без координат границ' in text:
        data['Координаты границ'] = 'Без координат границ'
    else:
        data['Координаты границ'] = 'С координатами границ'

    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line in fields:
            if i + 1 < len(lines):
                data[line] = lines[i + 1].strip()
            i += 1
        i += 1
    return data


def save_to_xlsx(data_list, filename):
    """
    Сохраняет список словарей data_list в Excel-файл.
    Заголовки формируются как объединение всех ключей из всех словарей.
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    all_keys = set()
    for data in data_list:
        all_keys.update(data.keys())
    header = sorted(list(all_keys))
    ws.append(header)

    for data in data_list:
        row = [data.get(key, "") for key in header]
        ws.append(row)

    wb.save(filename)


def save_to_json(data_list, filename):
    """
    Сохраняет список словарей data_list в JSON-файл.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Парсинг данных ЕГРН по кадастровым номерам")
    parser.add_argument("input_file", help="Путь к входному файлу формата JSON с кадастровыми номерами")
    parser.add_argument(
        "-o", "--output", default="земельный_участок.xlsx",
        help="Путь к выходному файлу (по умолчанию: земельный_участок.xlsx)"
    )
    parser.add_argument(
        "-f", "--format", choices=["json", "xlsx"], default="xlsx",
        help="Выходной формат (json или xlsx, по умолчанию xlsx)"
    )
    args = parser.parse_args()

    # Чтение входного JSON файла с кадастровыми номерами
    with open(args.input_file, "r", encoding="utf-8") as file:
        cad_numbers = json.load(file)

    results_list = []
    counter = 1
    for cad_number in cad_numbers:
        # Инициализация драйвера (при необходимости можно добавить headless-режим)
        driver = webdriver.Chrome()
        act = ActionChains(driver)

        # Получаем содержимое страницы по кадастровому номеру
        content = nspd_bot(cad_number, driver, act)
        driver.quit()

        # Парсинг данных и добавление в список результатов
        parsed_data = parse_egrn_data(content)
        results_list.append(parsed_data)

        print(f'Данные для {cad_number} успешно обработаны ({counter}/{len(cad_numbers)}).')
        counter += 1

    # Сохранение результатов в выбранном формате
    if args.format == "xlsx":
        save_to_xlsx(results_list, args.output)
    elif args.format == "json":
        save_to_json(results_list, args.output)
    print(f'\nВсе данные сохранены в файл: {args.output}')


if __name__ == "__main__":
    main()
