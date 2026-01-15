"""Есть директория data/, содержащая множество .json файлов. Каждый должен соответствовать схеме: 
json
1
2
3
4
5
{
  "id": integer,
  "tags": [string],
  "active": boolean
}
Напишите программу, которая: 
•	Проходит по всем .json файлам в директории. 
•	Проверяет соответствие схеме. 
•	Если поле отсутствует или имеет неверный тип — пытается исправить: 
o	Если id строка → преобразует в int (если возможно). 
o	Если tags не массив → делает пустой массив. 
o	Если active отсутствует → ставит false.
•	Сохраняет исправленные файлы в data_fixed/. 
•	Логирует ошибки в errors.log (в формате TXT).
"""

import json
from pathlib import Path

def fix_data(data):
    result = {}

    if 'id' in data:
        try:
            result['id'] = int(data['id'])
        except:
            result['id'] = 0
    else:
        result['id'] = 0
    
    if 'tags' in data and isinstance(data['tags'], list):
        result['tags'] = [str(tag) for tag in data['tags'] if tag is not None]
    else:
        result['tags'] = []
    
    if 'active' in data and isinstance(data['active'], bool):
        result['active'] = data['active']
    else:
        result['active'] = False
    
    return result

def process_files():
    with open('errors.log', 'w') as log_file:
        for filename in Path('data').glob('*.json'):
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                fixed = fix_data(data)
                with open(Path('data_fixed') / filename.name, 'w') as f:
                    json.dump(fixed, f, indent=2)

                log_file.write(f"{filename.name}\n")
                
            except json.JSONDecodeError:
                log_file.write(f"ERROR: {filename.name} - невалидный JSON\n")
            except Exception as e:
                log_file.write(f"ERROR: {filename.name} - {str(e)}\n")

if __name__ == "__main__":
    process_files()