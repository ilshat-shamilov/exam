from collections import defaultdict


def find_duplicates(input_file, output_file):
    line_counts = defaultdict(int)
    
    with open(input_file, 'r') as f:
        for line in f:
            line_counts[line] += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        for line, count in line_counts.items():
            if count > 1:
                f.write(line)


if __name__ == "__main__":
    find_duplicates(input_file='logs.txt', output_file='duplicates.txt')