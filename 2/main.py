""""Дан текстовый файл logs.txt, содержащий по одной строке лога на каждой строке (до нескольких миллионов строк).
Реализуйте программу, которая: 
•	Находит все строки, встречающиеся более одного раза. 
•	Выводит их в файл duplicates.txt, каждая строка — один раз.
Требования к эффективности: использовать минимально возможную память (например, через внешнюю сортировку или потоковую обработку, если файл очень большой). Для базовой версии допустимо загрузить всё в память.
"""
# потоковая обработка
def find_duplicates():
    seen = set()
    duplicates = set()
    
    with open('logs.txt', 'r') as f_in, open('duplicates.txt', 'w') as f_out:
        for line in f_in:
            if line in seen:
                if line not in duplicates:
                    duplicates.add(line)
                    f_out.write(line)
            else:
                seen.add(line)

if __name__ == "__main__":
    find_duplicates()