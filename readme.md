# NSPD Data Parser

## Русская версия

### Описание
Этот скрипт предназначен для парсинга данных ЕГРН по кадастровым номерам. На вход подается JSON-файл, содержащий список кадастровых номеров, а на выходе можно получить данные в формате **XLSX** или **JSON**.

### Требования

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

### Структура файлов

- `bot.py`: Содержит функцию `nspd_bot`, которая открывает сайт, осуществляет необходимые действия и возвращает текстовое содержимое страницы.
- `config.py`: Файл конфигурации, содержащий, например, переменную `fields` — список ключевых полей для парсинга.
- `script.py`: Основной скрипт, который осуществляет чтение входных данных, обработку и сохранение результатов.

### Формат входного файла

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

### Аргументы командной строки

- `input_file`: Путь к входному файлу JSON с кадастровыми номерами.
- `-o, --output`: Путь к выходному файлу (по умолчанию: `земельный_участок.xlsx`).
- `-f, --format`: Выходной формат данных. Допустимые значения:
  - `xlsx` – сохранение в Excel (по умолчанию)
  - `json` – сохранение в JSON

### Примеры использования

**Сохранение в Excel**:
```bash
python script.py cad_numbers.json -o result.xlsx -f xlsx
```

**Сохранение в JSON**:
```bash
python script.py cad_numbers.json -o result.json -f json
```

### Как работает скрипт

1. **Чтение входного файла**: Скрипт считывает список кадастровых номеров из указанного JSON-файла.
2. **Обработка данных**: Для каждого кадастрового номера:
   - Инициализируется Selenium WebDriver.
   - Вызывается функция `nspd_bot`, которая взаимодействует с сайтом и возвращает текстовую информацию.
   - Полученный текст парсится функцией `parse_egrn_data`, которая извлекает необходимые поля.
3. **Сохранение результатов**: Собранные данные сохраняются в указанный файл в формате XLSX или JSON.

### Примечания

- Для работы в headless-режиме можно модифицировать инициализацию драйвера в скрипте, добавив соответствующие опции.
- Убедитесь, что все зависимости установлены, а ChromeDriver настроен корректно.

---

## English Version

### Description
This script is designed for parsing EGRN data by cadastral numbers. It accepts a JSON file containing a list of cadastral numbers as input, and outputs data in either **XLSX** or **JSON** format.

### Requirements

- Python 3.6+
- [Selenium](https://pypi.org/project/selenium/)
  ```bash
  pip install selenium
  ```
- OpenPyXL
  ```bash
  pip install openpyxl
  ```
- ChromeDriver for Google Chrome  
  Ensure that the ChromeDriver version matches your installed browser version and is in the PATH.

### File Structure

- `bot.py`: Contains the `nspd_bot` function which opens the website, performs necessary actions, and returns the page's text content.
- `config.py`: Configuration file that may include variables like `fields` – a list of key fields for parsing.
- `script.py`: Main script that reads the input data, processes it, and saves the results.

### Input File Format

The input file should be in JSON format and contain a list of cadastral numbers. Example `cad_numbers.json`:

```json
[
  "31:05:1901001:831",
  "31:05:1901001:832",
  "31:05:1901001:978",
  "31:05:1901001:982",
  "31:05:1901001:985"
]
```

### Command-Line Arguments

- `input_file`: Path to the input JSON file with cadastral numbers.
- `-o, --output`: Path to the output file (default: `земельный_участок.xlsx`).
- `-f, --format`: Output data format. Allowed values:
  - `xlsx` – save as Excel (default)
  - `json` – save as JSON

### Usage Examples

**Saving as Excel**:
```bash
python script.py cad_numbers.json -o result.xlsx -f xlsx
```

**Saving as JSON**:
```bash
python script.py cad_numbers.json -o result.json -f json
```

### How the Script Works

1. **Reading the Input File**: The script reads a list of cadastral numbers from the specified JSON file.
2. **Data Processing**: For each cadastral number:
   - A Selenium WebDriver is initialized.
   - The `nspd_bot` function is called to interact with the website and retrieve textual information.
   - The retrieved text is parsed by the `parse_egrn_data` function to extract the necessary fields.
3. **Saving the Results**: The collected data is saved to the specified file in either XLSX or JSON format.

### Notes

- For headless mode, you can modify the WebDriver initialization in the script by adding the appropriate options.
- Ensure that all dependencies are installed and that ChromeDriver is properly configured.

---

## About the Author / Об авторе

I'm [Glebushnik](https://github.com/glebushnik/nspd-parser)  
I am the author of this project. Feel free to check out my GitHub repository for more information.
