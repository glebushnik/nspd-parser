import argparse
from nspd_parser import nspd_bot, parse_egrn_data

def main():
    parser = argparse.ArgumentParser(description="Парсер ЕГРН")
    parser.add_argument("input_file", help="Путь к JSON файлу с кадастровыми номерами")
    parser.add_argument("-o", "--output", default="земельный_участок.xlsx", help="Путь к выходному файлу")
    parser.add_argument("-f", "--format", choices=["xlsx", "json"], default="xlsx", help="Формат выходного файла")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
