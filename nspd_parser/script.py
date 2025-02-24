import json
import argparse
from pathlib import Path

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


def init_xlsx(filename):
    """Инициализирует XLSX файл с заголовками"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Кадастровый номер", "Адрес", "Площадь", "Координаты границ", "Статус"])
    wb.save(filename)


def append_to_xlsx(data, filename):
    """Добавляет запись в XLSX файл"""
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    row = [
        data.get('Кадастровый номер', ''),
        data.get('Адрес', ''),
        data.get('Площадь', ''),
        data.get('Координаты границ', ''),
        data.get('Статус', '')
    ]
    ws.append(row)
    wb.save(filename)


def append_to_json(data, filename):
    """Добавляет запись в JSON файл"""
    records = []
    if Path(filename).exists():
        with open(filename, "r", encoding="utf-8") as f:
            records = json.load(f)

    records.append(data)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Парсинг данных ЕГРН")
    parser.add_argument("input_file", help="JSON файл с кадастровыми номерами")
    parser.add_argument("-o", "--output", default="output.xlsx",
                        help="Выходной файл (по умолчанию: output.xlsx)")
    parser.add_argument("-f", "--format", choices=["json", "xlsx"], default="xlsx",
                        help="Формат вывода (по умолчанию: xlsx)")
    args = parser.parse_args()

    # Инициализация файла
    if args.format == "xlsx":
        init_xlsx(args.output)
    elif args.format == "json" and not Path(args.output).exists():
        with open(args.output, "w") as f:
            json.dump([], f)

    with open(args.input_file, "r", encoding="utf-8") as f:
        cad_numbers = json.load(f)

    for i, cad_number in enumerate(cad_numbers, 1):
        try:
            driver = webdriver.Chrome()
            act = ActionChains(driver)

            content = nspd_bot(cad_number, driver, act)
            parsed_data = parse_egrn_data(content)

            if args.format == "xlsx":
                append_to_xlsx(parsed_data, args.output)
            elif args.format == "json":
                append_to_json(parsed_data, args.output)

            print(f"Обработано {i}/{len(cad_numbers)}: {cad_number}")

        except Exception as e:
            print(f"Ошибка при обработке {cad_number}: {str(e)}")
        finally:
            driver.quit()


if __name__ == "__main__":
    main()
