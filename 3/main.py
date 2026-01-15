"""Напишите утилиту командной строки, которая принимает путь к файлу и конвертирует его между форматами:
config.yaml → config.json
или
settings.json → settings.csv (если данные табличные)
Поддерживаемые преобразования: 
•	YAML ↔ JSON 
•	JSON ↔ CSV (только если JSON — массив объектов с одинаковыми ключами)
"""

import sys
import json
import yaml
import csv

def convert_file(input_file, output_file):
    if input_file.endswith('.yaml') or input_file.endswith('.yml'):
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
        
        if output_file.endswith('.json'):
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=2)
        
    
    elif input_file.endswith('.json'):
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        if output_file.endswith('.yaml') or output_file.endswith('.yml'):
            with open(output_file, 'w') as f:
                yaml.dump(data, f)
        
        elif output_file.endswith('.csv'):
            with open(output_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
    
    elif input_file.endswith('.csv'):
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        print(reader)
        print(data)
        
        if output_file.endswith('.json'):
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=2)


def main():
    input_file, output_file = sys.argv[1], sys.argv[2]
    
    try:
        convert_file(input_file, output_file)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()