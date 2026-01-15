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