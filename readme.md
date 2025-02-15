# EGRN Data Parser

Этот скрипт предназначен для парсинга данных ЕГРН по кадастровым номерам. На вход подается JSON-файл, содержащий список кадастровых номеров, а на выходе можно получить данные в формате **XLSX** или **JSON**.

## Требования

- Python 3.6+
- [Selenium](https://pypi.org/project/selenium/)
  ```bash
  pip install selenium
  ```
- OpenPyXL
  ```bash
  pip install openpyxl
  ```
- ChromeDriver для Google Chrome  
  Убедитесь, что версия ChromeDriver соответствует установленной версии браузера и он находится в PATH.

## Структура файлов

- `bot.py`: Содержит функцию `nspd_bot`, которая открывает сайт, осуществляет необходимые действия и возвращает текстовое содержимое страницы.
- `config.py`: Файл конфигурации, содержащий, например, переменную `fields` — список ключевых полей для парсинга.
- `script.py`: Основной скрипт, который осуществляет чтение входных данных, обработку и сохранение результатов.

## Формат входного файла

Входной файл должен быть в формате JSON и содержать список кадастровых номеров. Пример файла `cad_numbers.json`:

```json
[
  "31:05:1901001:831",
  "31:05:1901001:832",
  "31:05:1901001:978",
  "31:05:1901001:982",
  "31:05:1901001:985"
]
```

## Аргументы командной строки

- `input_file`: Путь к входному файлу JSON с кадастровыми номерами.
- `-o, --output`: Путь к выходному файлу (по умолчанию: `земельный_участок.xlsx`).
- `-f, --format`: Выходной формат данных. Допустимые значения:
  - `xlsx` – сохранение в Excel (по умолчанию)
  - `json` – сохранение в JSON

## Примеры использования

**Сохранение в Excel**:
```bash
python script.py cad_numbers.json -o result.xlsx -f xlsx
```

**Сохранение в JSON**:
```bash
python script.py cad_numbers.json -o result.json -f json
```

## Как работает скрипт

1. **Чтение входного файла**: Скрипт считывает список кадастровых номеров из указанного JSON-файла.
2. **Обработка данных**: Для каждого кадастрового номера:
   - Инициализируется Selenium WebDriver
   - Вызывается функция `nspd_bot`, которая взаимодействует с сайтом и возвращает текстовую информацию
   - Полученный текст парсится функцией `parse_egrn_data`, которая извлекает необходимые поля
3. **Сохранение результатов**: Собранные данные сохраняются в указанный файл в формате XLSX или JSON.

## Примечания

- Для работы в headless-режиме можно модифицировать инициализацию драйвера в скрипте, добавив соответствующие опции.
- Убедитесь, что все зависимости установлены, а ChromeDriver настроен корректно.