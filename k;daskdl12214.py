import sys
from collections import defaultdict

def parse_log_line(line):
    parts = line.strip().split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path):
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs, level):
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

def display_log_details(logs):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level}':")
        display_log_details(filtered_logs)

if __name__ == "__main__":
    main()
